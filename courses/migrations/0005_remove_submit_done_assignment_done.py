# Generated by Django 4.1.2 on 2022-12-26 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_remove_course_assignment_remove_course_tutorial_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='submit',
            name='done',
        ),
        migrations.AddField(
            model_name='assignment',
            name='done',
            field=models.BooleanField(default=False),
        ),
    ]
