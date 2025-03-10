# Generated by Django 5.1 on 2025-02-03 08:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0003_alter_library_bookname_alter_library_studentname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='library',
            name='bookname',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testapp.book'),
        ),
        migrations.AlterField(
            model_name='library',
            name='studentname',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testapp.student'),
        ),
    ]
