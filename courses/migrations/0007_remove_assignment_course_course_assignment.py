# Generated by Django 4.1.2 on 2022-12-26 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0006_remove_course_assignment_assignment_course'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='assignment',
            name='course',
        ),
        migrations.AddField(
            model_name='course',
            name='assignment',
            field=models.ManyToManyField(blank=True, to='courses.assignment'),
        ),
    ]
