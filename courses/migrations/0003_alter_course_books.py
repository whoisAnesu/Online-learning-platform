# Generated by Django 4.1.2 on 2022-12-22 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_remove_course_books_course_books'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='books',
            field=models.ManyToManyField(blank=True, to='courses.book'),
        ),
    ]
