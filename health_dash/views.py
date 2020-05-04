from django.shortcuts import render
from django.db import connection
from django.core.serializers import serialize
from django.contrib.gis.db import models

from .models import Corporatorward,MumbaiHospital
from .forms import QueryForm
from django.http import JsonResponse
# Create your views here.
class Test():
    template_name = "about.html"

# SELECT a.uniq_id,sum(b.dummy_bed_count) as total_bed_count,count(b.facility_n) as hospital_count
# FROM corporatorward a
# INNER JOIN mumbai_hospital b 
# ON a.uniq_id = b.uniq_id
# GROUP BY a.uniq_id


class MyTest(models.Model):
    id = models.IntegerField(primary_key=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    dummy_total_pop = models.IntegerField(blank=True, null=True)
    uniq_id = models.CharField(max_length=15, blank=True, null=True)
    total_bed_count = models.IntegerField(blank=True, null=True)
    hospital_count=models.IntegerField(blank=True, null=True)

def healthDash(request):
    return render(request,"health_dash/health.html")

def qb(request):
    # cw = models.Corporatorward.objects.values_list('uniq_id')
    cw = Corporatorward.objects.all()
    mh = MumbaiHospital.objects.all()
    cursor = connection.cursor()
    # name_map = {'id': 'id', 'geom': 'geom', 'dummy_total_pop': 'dummy_total_pop', 'uniq_id': 'uniq_id','total_bed_count':'total_bed_count','hospital_count':'hospital_count'}
    raw = MyTest.objects.raw("""select  ROW_NUMBER() OVER (ORDER BY b.total_bed_count) AS id, a.geom, a.dummy_total_pop,a.uniq_id , b.total_bed_count ::int,b.hospital_count 
                    from corporatorward a
                    inner join (SELECT a.uniq_id,sum(b.dummy_bed_count) as total_bed_count,count(b.facility_n) as hospital_count
                    FROM corporatorward a
                    INNER JOIN mumbai_hospital b 
                    ON a.uniq_id = b.uniq_id
                    GROUP BY a.uniq_id) b 
                    on a.uniq_id = b.uniq_id""")
    # cursor.execute("""select a.geom, a.dummy_total_pop,a.uniq_id , b.total_bed_count,b.hospital_count 
    #                 from corporatorward a
    #                 inner join (SELECT a.uniq_id,sum(b.dummy_bed_count) as total_bed_count,count(b.facility_n) as hospital_count
    #                 FROM corporatorward a
    #                 INNER JOIN mumbai_hospital b 
    #                 ON a.uniq_id = b.uniq_id
    #                 GROUP BY a.uniq_id) b 
    #                 on a.uniq_id = b.uniq_id""")
    # raw = models.Corporatorward.objects.raw('SELECT * FROM corporatorward')
# ['id', 'geom', 'fid', 'name', 'census_cod', 'uniq_id', 'dummy_total_pop']
    # columns = [col[0] for col in cursor.description]
    # rows = cursor.fetchall()
#    fields=('id', 'geom', 'dummy_total_pop', 'uniq_id', 'total_bed_count', 'hospital_count')
    ser_test = serialize('geojson', raw,)

    context = {'data':ser_test}
    return render(request,"health_dash/test.html",context)


def interface(request):
    myform = QueryForm()
    if request.method == 'POST':
        myform =  QueryForm(request.POST)
        if myform.is_valid():
            query_column = myform.cleaned_data['field']
            operator = myform.cleaned_data['operator']
            value = myform.cleaned_data['value']
            query="""select * from corporatorward where {} {} {}""".format(query_column,operator,value)
            raw = Corporatorward.objects.raw(query)
            context = {'form':myform,'data':raw}
            return render(request,'health_dash/interface.html',context)

        else:
            print(myform.errors)

    context = {'form':myform}
    return render(request,'health_dash/interface.html',context)