# Generated by Django 3.0.5 on 2020-04-29 14:43

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('health_dash', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyTest',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(blank=True, null=True, srid=4326)),
                ('dummy_total_pop', models.IntegerField(blank=True, null=True)),
                ('uniq_id', models.CharField(blank=True, max_length=15, null=True)),
                ('total_bed_count', models.IntegerField(blank=True, null=True)),
                ('hospital_count', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
