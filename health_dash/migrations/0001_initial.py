# Generated by Django 3.0.5 on 2020-04-28 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Corporatorward',
            fields=[
                ('id', models.DecimalField(decimal_places=65535, max_digits=65535, primary_key=True, serialize=False)),
                ('geom', models.TextField(blank=True, null=True)),
                ('fid', models.BigIntegerField(blank=True, null=True)),
                ('name', models.CharField(blank=True, max_length=254, null=True)),
                ('census_cod', models.CharField(blank=True, max_length=80, null=True)),
                ('uniq_id', models.CharField(blank=True, max_length=15, null=True)),
                ('dummy_total_pop', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'corporatorward',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MumbaiHospital',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('geom', models.TextField(blank=True, null=True)),
                ('facility_n', models.CharField(blank=True, max_length=254, null=True)),
                ('address_field', models.CharField(blank=True, db_column='address _', max_length=254, null=True)),
                ('address_field_0', models.DecimalField(blank=True, db_column='address _/', decimal_places=65535, max_digits=65535, null=True)),
                ('address_1', models.DecimalField(blank=True, db_column='address _1', decimal_places=65535, max_digits=65535, null=True)),
                ('address_2', models.DecimalField(blank=True, db_column='address _2', decimal_places=65535, max_digits=65535, null=True)),
                ('address_te', models.CharField(blank=True, db_column='address(te', max_length=254, null=True)),
                ('address_di', models.CharField(blank=True, db_column='address(di', max_length=254, null=True)),
                ('address_pl', models.CharField(blank=True, db_column='address(pl', max_length=254, null=True)),
                ('field_address_p', models.DecimalField(blank=True, db_column='_address(p', decimal_places=65535, max_digits=65535, null=True)),
                ('field_address_1', models.DecimalField(blank=True, db_column='_address_1', decimal_places=65535, max_digits=65535, null=True)),
                ('field_address_2', models.DecimalField(blank=True, db_column='_address_2', decimal_places=65535, max_digits=65535, null=True)),
                ('field_address_3', models.DecimalField(blank=True, db_column='_address_3', decimal_places=65535, max_digits=65535, null=True)),
                ('category_o', models.CharField(blank=True, db_column='category o', max_length=254, null=True)),
                ('facility_t', models.CharField(blank=True, db_column='facility t', max_length=254, null=True)),
                ('facility_1', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('facility_2', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('facility_3', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('facility_4', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('facility_5', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('facility_6', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('facility_7', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('facility_8', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('facility_9', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('facility10', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('facility11', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('facility12', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('facility13', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('facility14', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('facility15', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('facility16', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('facility17', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('specify_field', models.CharField(blank=True, db_column='specify _', max_length=254, null=True)),
                ('specify_th', models.CharField(blank=True, db_column='specify th', max_length=254, null=True)),
                ('specify_1', models.DecimalField(blank=True, db_column='specify _1', decimal_places=65535, max_digits=65535, null=True)),
                ('specify_2', models.DecimalField(blank=True, db_column='specify _2', decimal_places=65535, max_digits=65535, null=True)),
                ('specify_3', models.DecimalField(blank=True, db_column='specify _3', decimal_places=65535, max_digits=65535, null=True)),
                ('specify_4', models.DecimalField(blank=True, db_column='specify _4', decimal_places=65535, max_digits=65535, null=True)),
                ('specify_5', models.DecimalField(blank=True, db_column='specify _5', decimal_places=65535, max_digits=65535, null=True)),
                ('specify_6', models.DecimalField(blank=True, db_column='specify _6', decimal_places=65535, max_digits=65535, null=True)),
                ('specify_7', models.DecimalField(blank=True, db_column='specify _7', decimal_places=65535, max_digits=65535, null=True)),
                ('is_pharmac', models.CharField(blank=True, db_column='is pharmac', max_length=254, null=True)),
                ('is_optical', models.CharField(blank=True, db_column='is optical', max_length=254, null=True)),
                ('specify_8', models.CharField(blank=True, db_column='specify _8', max_length=254, null=True)),
                ('facility_m', models.CharField(blank=True, db_column='facility m', max_length=254, null=True)),
                ('facility18', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('facility19', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('facility20', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('facility21', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('specify_if', models.CharField(blank=True, db_column='specify(if', max_length=254, null=True)),
                ('specify_1_0', models.CharField(blank=True, db_column='specify(_1', max_length=254, null=True)),
                ('facility_b', models.CharField(blank=True, db_column='facility b', max_length=254, null=True)),
                ('facility22', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('facility23', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('facility24', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('if_other_b', models.CharField(blank=True, db_column='if other b', max_length=254, null=True)),
                ('service_da', models.CharField(blank=True, db_column='service da', max_length=254, null=True)),
                ('service_1', models.DecimalField(blank=True, db_column='service _1', decimal_places=65535, max_digits=65535, null=True)),
                ('service_2', models.DecimalField(blank=True, db_column='service _2', decimal_places=65535, max_digits=65535, null=True)),
                ('service_3', models.DecimalField(blank=True, db_column='service _3', decimal_places=65535, max_digits=65535, null=True)),
                ('specify_9', models.DecimalField(blank=True, db_column='specify _9', decimal_places=65535, max_digits=65535, null=True)),
                ('facility_s', models.CharField(blank=True, db_column='facility s', max_length=254, null=True)),
                ('facility25', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('facility26', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('facility27', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('facility28', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('specify_10', models.CharField(blank=True, db_column='specify 10', max_length=254, null=True)),
                ('specify_11', models.DecimalField(blank=True, db_column='specify 11', decimal_places=65535, max_digits=65535, null=True)),
                ('specify_12', models.DecimalField(blank=True, db_column='specify 12', decimal_places=65535, max_digits=65535, null=True)),
                ('availabili', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('service_li', models.CharField(blank=True, db_column='service li', max_length=254, null=True)),
                ('service_4', models.DecimalField(blank=True, db_column='service _4', decimal_places=65535, max_digits=65535, null=True)),
                ('service_5', models.DecimalField(blank=True, db_column='service _5', decimal_places=65535, max_digits=65535, null=True)),
                ('service_6', models.DecimalField(blank=True, db_column='service _6', decimal_places=65535, max_digits=65535, null=True)),
                ('specify_13', models.CharField(blank=True, db_column='specify 13', max_length=254, null=True)),
                ('specify_f', models.CharField(blank=True, db_column='specify (f', max_length=254, null=True)),
                ('specify_14', models.DecimalField(blank=True, db_column='specify 14', decimal_places=65535, max_digits=65535, null=True)),
                ('specify_15', models.DecimalField(blank=True, db_column='specify 15', decimal_places=65535, max_digits=65535, null=True)),
                ('specify_16', models.CharField(blank=True, db_column='specify 16', max_length=254, null=True)),
                ('specify_17', models.DecimalField(blank=True, db_column='specify 17', decimal_places=65535, max_digits=65535, null=True)),
                ('specify_18', models.DecimalField(blank=True, db_column='specify 18', decimal_places=65535, max_digits=65535, null=True)),
                ('specify_19', models.DecimalField(blank=True, db_column='specify 19', decimal_places=65535, max_digits=65535, null=True)),
                ('amenities', models.CharField(blank=True, max_length=254, null=True)),
                ('amenities_field', models.DecimalField(blank=True, db_column='amenities/', decimal_places=65535, max_digits=65535, null=True)),
                ('amenitie_1', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('amenitie_2', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('amenitie_3', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('amenitie_4', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('amenitie_5', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('specify_field_0', models.CharField(blank=True, db_column='specify __', max_length=254, null=True)),
                ('if_availab', models.CharField(blank=True, db_column='if availab', max_length=254, null=True)),
                ('specify', models.CharField(blank=True, max_length=254, null=True)),
                ('specify_20', models.CharField(blank=True, db_column='specify 20', max_length=254, null=True)),
                ('is_interne', models.CharField(blank=True, db_column='is interne', max_length=254, null=True)),
                ('can_you_ge', models.CharField(blank=True, db_column='can you ge', max_length=254, null=True)),
                ('specify_21', models.CharField(blank=True, db_column='specify 21', max_length=254, null=True)),
                ('field_specify_t', models.CharField(blank=True, db_column='_specify t', max_length=254, null=True)),
                ('field_specify_1', models.CharField(blank=True, db_column='_specify_1', max_length=254, null=True)),
                ('field_specify_2', models.CharField(blank=True, db_column='_specify_2', max_length=254, null=True)),
                ('field_specify_3', models.CharField(blank=True, db_column='_specify_3', max_length=254, null=True)),
                ('specify_22', models.CharField(blank=True, db_column='specify 22', max_length=254, null=True)),
                ('field_specify_4', models.CharField(blank=True, db_column='_specify_4', max_length=254, null=True)),
                ('field_specify_5', models.CharField(blank=True, db_column='_specify_5', max_length=254, null=True)),
                ('field_specify_6', models.CharField(blank=True, db_column='_specify_6', max_length=254, null=True)),
                ('field_specify_7', models.CharField(blank=True, db_column='_specify_7', max_length=254, null=True)),
                ('specify_23', models.CharField(blank=True, db_column='specify 23', max_length=254, null=True)),
                ('specify_field_1', models.CharField(blank=True, db_column='specify _.', max_length=254, null=True)),
                ('census_cod', models.CharField(blank=True, max_length=80, null=True)),
                ('dummy_bed_count', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
            ],
            options={
                'db_table': 'mumbai_hospital',
                'managed': False,
            },
        ),
    ]
