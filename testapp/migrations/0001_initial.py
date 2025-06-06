# Generated by Django 5.1 on 2025-02-03 05:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('author', models.CharField(max_length=50)),
                ('publication', models.CharField(max_length=120)),
                ('year', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('Class', models.IntegerField()),
                ('photo', models.CharField(default='images/default.webp', max_length=150)),
                ('video', models.CharField(default='images/default.webp', max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Library',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('bookname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testapp.book')),
                ('studentname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testapp.student')),
            ],
        ),
    ]
