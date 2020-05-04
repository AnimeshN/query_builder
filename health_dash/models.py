# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Corporatorward(models.Model):
    id = models.DecimalField(primary_key=True, max_digits=65535, decimal_places=65535)
    geom = models.TextField(blank=True, null=True)  # This field type is a guess.
    fid = models.BigIntegerField(blank=True, null=True)
    name = models.CharField(max_length=254, blank=True, null=True)
    census_cod = models.CharField(max_length=80, blank=True, null=True)
    uniq_id = models.CharField(max_length=15, blank=True, null=True)
    dummy_total_pop = models.IntegerField(blank=True, null=True)

    # def __str__(self):
    #     return self.name
    class Meta:
        managed = False
        db_table = 'corporatorward'


class MumbaiHospital(models.Model):
    id = models.IntegerField(primary_key=True)
    geom = models.TextField(blank=True, null=True)  # This field type is a guess.
    facility_n = models.CharField(max_length=254, blank=True, null=True)
    address_field = models.CharField(db_column='address _', max_length=254, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    address_field_0 = models.DecimalField(db_column='address _/', max_digits=65535, decimal_places=65535, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'. Field renamed because of name conflict.
    address_1 = models.DecimalField(db_column='address _1', max_digits=65535, decimal_places=65535, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    address_2 = models.DecimalField(db_column='address _2', max_digits=65535, decimal_places=65535, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    address_te = models.CharField(db_column='address(te', max_length=254, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    address_di = models.CharField(db_column='address(di', max_length=254, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    address_pl = models.CharField(db_column='address(pl', max_length=254, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    field_address_p = models.DecimalField(db_column='_address(p', max_digits=65535, decimal_places=65535, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    field_address_1 = models.DecimalField(db_column='_address_1', max_digits=65535, decimal_places=65535, blank=True, null=True)  # Field renamed because it started with '_'.
    field_address_2 = models.DecimalField(db_column='_address_2', max_digits=65535, decimal_places=65535, blank=True, null=True)  # Field renamed because it started with '_'.
    field_address_3 = models.DecimalField(db_column='_address_3', max_digits=65535, decimal_places=65535, blank=True, null=True)  # Field renamed because it started with '_'.
    category_o = models.CharField(db_column='category o', max_length=254, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    facility_t = models.CharField(db_column='facility t', max_length=254, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    facility_1 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    facility_2 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    facility_3 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    facility_4 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    facility_5 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    facility_6 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    facility_7 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    facility_8 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    facility_9 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    facility10 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    facility11 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    facility12 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    facility13 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    facility14 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    facility15 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    facility16 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    facility17 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    specify_field = models.CharField(db_column='specify _', max_length=254, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    specify_th = models.CharField(db_column='specify th', max_length=254, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    specify_1 = models.DecimalField(db_column='specify _1', max_digits=65535, decimal_places=65535, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    specify_2 = models.DecimalField(db_column='specify _2', max_digits=65535, decimal_places=65535, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    specify_3 = models.DecimalField(db_column='specify _3', max_digits=65535, decimal_places=65535, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    specify_4 = models.DecimalField(db_column='specify _4', max_digits=65535, decimal_places=65535, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    specify_5 = models.DecimalField(db_column='specify _5', max_digits=65535, decimal_places=65535, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    specify_6 = models.DecimalField(db_column='specify _6', max_digits=65535, decimal_places=65535, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    specify_7 = models.DecimalField(db_column='specify _7', max_digits=65535, decimal_places=65535, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    is_pharmac = models.CharField(db_column='is pharmac', max_length=254, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    is_optical = models.CharField(db_column='is optical', max_length=254, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    specify_8 = models.CharField(db_column='specify _8', max_length=254, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    facility_m = models.CharField(db_column='facility m', max_length=254, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    facility18 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    facility19 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    facility20 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    facility21 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    specify_if = models.CharField(db_column='specify(if', max_length=254, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    specify_1_0 = models.CharField(db_column='specify(_1', max_length=254, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because of name conflict.
    facility_b = models.CharField(db_column='facility b', max_length=254, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    facility22 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    facility23 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    facility24 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    if_other_b = models.CharField(db_column='if other b', max_length=254, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    service_da = models.CharField(db_column='service da', max_length=254, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    service_1 = models.DecimalField(db_column='service _1', max_digits=65535, decimal_places=65535, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    service_2 = models.DecimalField(db_column='service _2', max_digits=65535, decimal_places=65535, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    service_3 = models.DecimalField(db_column='service _3', max_digits=65535, decimal_places=65535, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    specify_9 = models.DecimalField(db_column='specify _9', max_digits=65535, decimal_places=65535, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    facility_s = models.CharField(db_column='facility s', max_length=254, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    facility25 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    facility26 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    facility27 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    facility28 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    specify_10 = models.CharField(db_column='specify 10', max_length=254, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    specify_11 = models.DecimalField(db_column='specify 11', max_digits=65535, decimal_places=65535, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    specify_12 = models.DecimalField(db_column='specify 12', max_digits=65535, decimal_places=65535, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    availabili = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    service_li = models.CharField(db_column='service li', max_length=254, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    service_4 = models.DecimalField(db_column='service _4', max_digits=65535, decimal_places=65535, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    service_5 = models.DecimalField(db_column='service _5', max_digits=65535, decimal_places=65535, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    service_6 = models.DecimalField(db_column='service _6', max_digits=65535, decimal_places=65535, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    specify_13 = models.CharField(db_column='specify 13', max_length=254, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    specify_f = models.CharField(db_column='specify (f', max_length=254, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    specify_14 = models.DecimalField(db_column='specify 14', max_digits=65535, decimal_places=65535, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    specify_15 = models.DecimalField(db_column='specify 15', max_digits=65535, decimal_places=65535, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    specify_16 = models.CharField(db_column='specify 16', max_length=254, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    specify_17 = models.DecimalField(db_column='specify 17', max_digits=65535, decimal_places=65535, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    specify_18 = models.DecimalField(db_column='specify 18', max_digits=65535, decimal_places=65535, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    specify_19 = models.DecimalField(db_column='specify 19', max_digits=65535, decimal_places=65535, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    amenities = models.CharField(max_length=254, blank=True, null=True)
    amenities_field = models.DecimalField(db_column='amenities/', max_digits=65535, decimal_places=65535, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    amenitie_1 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    amenitie_2 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    amenitie_3 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    amenitie_4 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    amenitie_5 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    specify_field_0 = models.CharField(db_column='specify __', max_length=254, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it contained more than one '_' in a row. Field renamed because it ended with '_'. Field renamed because of name conflict.
    if_availab = models.CharField(db_column='if availab', max_length=254, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    specify = models.CharField(max_length=254, blank=True, null=True)
    specify_20 = models.CharField(db_column='specify 20', max_length=254, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    is_interne = models.CharField(db_column='is interne', max_length=254, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    can_you_ge = models.CharField(db_column='can you ge', max_length=254, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    specify_21 = models.CharField(db_column='specify 21', max_length=254, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    field_specify_t = models.CharField(db_column='_specify t', max_length=254, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    field_specify_1 = models.CharField(db_column='_specify_1', max_length=254, blank=True, null=True)  # Field renamed because it started with '_'.
    field_specify_2 = models.CharField(db_column='_specify_2', max_length=254, blank=True, null=True)  # Field renamed because it started with '_'.
    field_specify_3 = models.CharField(db_column='_specify_3', max_length=254, blank=True, null=True)  # Field renamed because it started with '_'.
    specify_22 = models.CharField(db_column='specify 22', max_length=254, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    field_specify_4 = models.CharField(db_column='_specify_4', max_length=254, blank=True, null=True)  # Field renamed because it started with '_'.
    field_specify_5 = models.CharField(db_column='_specify_5', max_length=254, blank=True, null=True)  # Field renamed because it started with '_'.
    field_specify_6 = models.CharField(db_column='_specify_6', max_length=254, blank=True, null=True)  # Field renamed because it started with '_'.
    field_specify_7 = models.CharField(db_column='_specify_7', max_length=254, blank=True, null=True)  # Field renamed because it started with '_'.
    specify_23 = models.CharField(db_column='specify 23', max_length=254, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    specify_field_1 = models.CharField(db_column='specify _.', max_length=254, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'. Field renamed because of name conflict.
    uniq_id = models.CharField(max_length=15, blank=True, null=True)
    # uniq_id = models.ForeignKey(Corporatorward, default=0, on_delete=models.SET_DEFAULT)
    census_cod = models.CharField(max_length=80, blank=True, null=True)
    dummy_bed_count = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mumbai_hospital'

# class MyTest(models.Model):
#     id = models.IntegerField(primary_key=True)
#     geom = models.MultiPolygonField(blank=True, null=True)
#     dummy_total_pop = models.IntegerField(blank=True, null=True)
#     uniq_id = models.CharField(max_length=15, blank=True, null=True)
#     total_bed_count = models.IntegerField(blank=True, null=True)
#     hospital_count=models.IntegerField(blank=True, null=True)
    