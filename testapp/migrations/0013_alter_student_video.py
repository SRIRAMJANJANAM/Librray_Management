# Generated by Django 5.1 on 2025-02-20 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0012_alter_student_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='video',
            field=models.FileField(default='videos/default.mp4', upload_to='videos/'),
        ),
    ]
