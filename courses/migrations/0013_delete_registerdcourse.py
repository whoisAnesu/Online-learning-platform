# Generated by Django 4.1.2 on 2023-02-08 16:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0012_registerdcourse_name'),
    ]

    operations = [
        migrations.DeleteModel(
            name='RegisterdCourse',
        ),
    ]
