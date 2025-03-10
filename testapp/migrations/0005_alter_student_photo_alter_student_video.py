# Generated by Django 5.1 on 2025-02-03 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0004_alter_library_bookname_alter_library_studentname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='photo',
            field=models.FileField(default='images/default.webp', upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='student',
            name='video',
            field=models.FileField(default='videos/default.webp', upload_to='images/'),
        ),
    ]
