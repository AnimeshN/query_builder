# Generated by Django 3.0.5 on 2020-04-29 14:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('health_dash', '0003_delete_mytest'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Corporatorward',
        ),
        migrations.DeleteModel(
            name='MumbaiHospital',
        ),
    ]