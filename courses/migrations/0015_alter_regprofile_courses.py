# Generated by Django 4.1.2 on 2023-05-14 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0014_regprofile_registration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='regprofile',
            name='courses',
            field=models.ManyToManyField(blank=True, to='courses.course'),
        ),
    ]
