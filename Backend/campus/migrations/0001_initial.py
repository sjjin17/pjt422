# Generated by Django 3.2.12 on 2022-07-22 07:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Campus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Floor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('map_path', models.TextField()),
                ('width', models.FloatField()),
                ('height', models.FloatField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('building', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='floor', to='campus.building')),
            ],
        ),
        migrations.CreateModel(
            name='Trashbin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=200)),
                ('trash_type', models.CharField(choices=[('GER', 'General'), ('PET', 'Plastic'), ('CAN', 'Can'), ('GLA', 'Glass'), ('PPR', 'Paper')], default='GER', max_length=3)),
                ('current_amount', models.FloatField()),
                ('total_amount', models.FloatField()),
                ('status', models.CharField(choices=[('SAF', 'Safe'), ('CAU', 'Caution'), ('WAR', 'Warning')], default='SAF', max_length=3)),
                ('location_x', models.FloatField()),
                ('location_y', models.FloatField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('discard_users', models.ManyToManyField(related_name='discard_trashbin', to=settings.AUTH_USER_MODEL)),
                ('floor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trashbin', to='campus.floor')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_num', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('belong', models.CharField(max_length=100)),
                ('rfid_num', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('campus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student', to='campus.campus')),
            ],
        ),
        migrations.AddField(
            model_name='building',
            name='campus',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='building', to='campus.campus'),
        ),
    ]
