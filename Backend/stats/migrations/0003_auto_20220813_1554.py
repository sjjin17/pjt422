# Generated by Django 3.2.12 on 2022-08-13 06:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0002_auto_20220813_1551'),
    ]

    operations = [
        migrations.RenameField(
            model_name='buildingdate',
            old_name='GRE',
            new_name='GER',
        ),
        migrations.RenameField(
            model_name='floordate',
            old_name='GRE',
            new_name='GER',
        ),
    ]
