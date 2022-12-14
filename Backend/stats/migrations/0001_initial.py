# Generated by Django 3.2.12 on 2022-08-17 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BuildingDate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('building_pk', models.IntegerField()),
                ('hour_00', models.IntegerField(default=0)),
                ('hour_01', models.IntegerField(default=0)),
                ('hour_02', models.IntegerField(default=0)),
                ('hour_03', models.IntegerField(default=0)),
                ('hour_04', models.IntegerField(default=0)),
                ('hour_05', models.IntegerField(default=0)),
                ('hour_06', models.IntegerField(default=0)),
                ('hour_07', models.IntegerField(default=0)),
                ('hour_08', models.IntegerField(default=0)),
                ('hour_09', models.IntegerField(default=0)),
                ('hour_10', models.IntegerField(default=0)),
                ('hour_11', models.IntegerField(default=0)),
                ('hour_12', models.IntegerField(default=0)),
                ('hour_13', models.IntegerField(default=0)),
                ('hour_14', models.IntegerField(default=0)),
                ('hour_15', models.IntegerField(default=0)),
                ('hour_16', models.IntegerField(default=0)),
                ('hour_17', models.IntegerField(default=0)),
                ('hour_18', models.IntegerField(default=0)),
                ('hour_19', models.IntegerField(default=0)),
                ('hour_20', models.IntegerField(default=0)),
                ('hour_21', models.IntegerField(default=0)),
                ('hour_22', models.IntegerField(default=0)),
                ('hour_23', models.IntegerField(default=0)),
                ('total', models.IntegerField(default=0)),
                ('year', models.CharField(max_length=4)),
                ('month', models.CharField(max_length=2)),
                ('date', models.CharField(max_length=2)),
                ('CAN', models.IntegerField(default=0)),
                ('GER', models.IntegerField(default=0)),
                ('GLA', models.IntegerField(default=0)),
                ('PET', models.IntegerField(default=0)),
                ('PPR', models.IntegerField(default=0)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FloorDate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('building_pk', models.IntegerField()),
                ('hour_00', models.IntegerField(default=0)),
                ('hour_01', models.IntegerField(default=0)),
                ('hour_02', models.IntegerField(default=0)),
                ('hour_03', models.IntegerField(default=0)),
                ('hour_04', models.IntegerField(default=0)),
                ('hour_05', models.IntegerField(default=0)),
                ('hour_06', models.IntegerField(default=0)),
                ('hour_07', models.IntegerField(default=0)),
                ('hour_08', models.IntegerField(default=0)),
                ('hour_09', models.IntegerField(default=0)),
                ('hour_10', models.IntegerField(default=0)),
                ('hour_11', models.IntegerField(default=0)),
                ('hour_12', models.IntegerField(default=0)),
                ('hour_13', models.IntegerField(default=0)),
                ('hour_14', models.IntegerField(default=0)),
                ('hour_15', models.IntegerField(default=0)),
                ('hour_16', models.IntegerField(default=0)),
                ('hour_17', models.IntegerField(default=0)),
                ('hour_18', models.IntegerField(default=0)),
                ('hour_19', models.IntegerField(default=0)),
                ('hour_20', models.IntegerField(default=0)),
                ('hour_21', models.IntegerField(default=0)),
                ('hour_22', models.IntegerField(default=0)),
                ('hour_23', models.IntegerField(default=0)),
                ('total', models.IntegerField(default=0)),
                ('year', models.CharField(max_length=4)),
                ('month', models.CharField(max_length=2)),
                ('date', models.CharField(max_length=2)),
                ('CAN', models.IntegerField(default=0)),
                ('GER', models.IntegerField(default=0)),
                ('GLA', models.IntegerField(default=0)),
                ('PET', models.IntegerField(default=0)),
                ('PPR', models.IntegerField(default=0)),
                ('floor_pk', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TrashbinDate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('building_pk', models.IntegerField()),
                ('hour_00', models.IntegerField(default=0)),
                ('hour_01', models.IntegerField(default=0)),
                ('hour_02', models.IntegerField(default=0)),
                ('hour_03', models.IntegerField(default=0)),
                ('hour_04', models.IntegerField(default=0)),
                ('hour_05', models.IntegerField(default=0)),
                ('hour_06', models.IntegerField(default=0)),
                ('hour_07', models.IntegerField(default=0)),
                ('hour_08', models.IntegerField(default=0)),
                ('hour_09', models.IntegerField(default=0)),
                ('hour_10', models.IntegerField(default=0)),
                ('hour_11', models.IntegerField(default=0)),
                ('hour_12', models.IntegerField(default=0)),
                ('hour_13', models.IntegerField(default=0)),
                ('hour_14', models.IntegerField(default=0)),
                ('hour_15', models.IntegerField(default=0)),
                ('hour_16', models.IntegerField(default=0)),
                ('hour_17', models.IntegerField(default=0)),
                ('hour_18', models.IntegerField(default=0)),
                ('hour_19', models.IntegerField(default=0)),
                ('hour_20', models.IntegerField(default=0)),
                ('hour_21', models.IntegerField(default=0)),
                ('hour_22', models.IntegerField(default=0)),
                ('hour_23', models.IntegerField(default=0)),
                ('total', models.IntegerField(default=0)),
                ('year', models.CharField(max_length=4)),
                ('month', models.CharField(max_length=2)),
                ('date', models.CharField(max_length=2)),
                ('token', models.CharField(max_length=20)),
                ('floor_pk', models.IntegerField()),
                ('trash_type', models.CharField(choices=[('GER', 'General'), ('PET', 'Plastic'), ('CAN', 'Can'), ('GLA', 'Glass'), ('PPR', 'Paper')], default='GER', max_length=3)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
