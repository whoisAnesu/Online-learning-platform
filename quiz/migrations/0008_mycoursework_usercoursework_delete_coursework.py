# Generated by Django 4.1.2 on 2023-05-17 11:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('quiz', '0007_remove_coursework_course_quiz_coursework_course_quiz'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mycoursework',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('the_course', models.CharField(blank=True, max_length=200, null=True)),
                ('the_mark', models.IntegerField(help_text='%')),
                ('the_remark', models.CharField(blank=True, max_length=200, null=True)),
                ('the_classification', models.CharField(blank=True, max_length=5, null=True)),
                ('course_quiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.quiz')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserCoursework',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mycoursework', models.ManyToManyField(to='quiz.mycoursework')),
            ],
        ),
        migrations.DeleteModel(
            name='Coursework',
        ),
    ]
