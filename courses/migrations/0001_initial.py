# Generated by Django 3.0.6 on 2020-12-20 20:50

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('image', models.ImageField(max_length=60, upload_to='category/')),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('body', models.TextField()),
                ('description', ckeditor.fields.RichTextField()),
                ('slug', models.SlugField(max_length=250, unique=True)),
                ('images', models.ImageField(blank=True, null=True, upload_to='courses/')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='courses', to='courses.Category')),
            ],
            options={
                'verbose_name': 'course',
                'verbose_name_plural': 'courses',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Leadership_board',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(blank=True, max_length=60)),
                ('score', models.IntegerField(blank=True)),
                ('course', models.CharField(blank=True, max_length=50)),
                ('date', models.DateField(blank=True)),
                ('last_renewal', models.DateField()),
                ('trials', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField()),
                ('description', models.TextField(blank=True, null=True)),
                ('duration', models.IntegerField()),
                ('time_denotation', models.CharField(choices=[('min', 'min'), ('hour', 'hour')], max_length=6)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.Courses')),
            ],
        ),
        migrations.CreateModel(
            name='QuizQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('question_mark', models.DecimalField(decimal_places=2, default=0, max_digits=6)),
                ('slug', models.SlugField()),
                ('A', models.CharField(max_length=500)),
                ('B', models.CharField(max_length=500)),
                ('C', models.CharField(max_length=500)),
                ('D', models.CharField(max_length=500)),
                ('correct_answer', models.CharField(choices=[('A', models.CharField(max_length=500)), ('B', models.CharField(max_length=500)), ('C', models.CharField(max_length=500)), ('D', models.CharField(max_length=500))], default=False, max_length=30)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.Courses')),
                ('quiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.Quiz')),
            ],
        ),
        migrations.CreateModel(
            name='QuizProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_score', models.DecimalField(decimal_places=2, default=0, max_digits=6)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='QuestionChoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('A', models.CharField(max_length=500)),
                ('B', models.CharField(max_length=500)),
                ('C', models.CharField(max_length=500)),
                ('D', models.CharField(max_length=500)),
                ('correct_answer', models.CharField(choices=[('A', models.CharField(max_length=500)), ('B', models.CharField(max_length=500)), ('C', models.CharField(max_length=500)), ('D', models.CharField(max_length=500))], default=False, max_length=30)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='options', to='courses.QuizQuestion')),
            ],
        ),
    ]
