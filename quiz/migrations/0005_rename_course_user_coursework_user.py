# Generated by Django 4.1.2 on 2023-05-16 16:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0004_alter_coursework_the_classification_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='coursework',
            old_name='course_user',
            new_name='user',
        ),
    ]
