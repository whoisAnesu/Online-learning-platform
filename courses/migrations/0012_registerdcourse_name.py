# Generated by Django 4.1.2 on 2023-02-08 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0011_remove_registerdcourse_course_registerdcourse_course'),
    ]

    operations = [
        migrations.AddField(
            model_name='registerdcourse',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
