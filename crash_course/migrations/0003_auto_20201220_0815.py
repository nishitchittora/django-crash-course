# Generated by Django 2.2.11 on 2020-12-20 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crash_course', '0002_auto_20201220_0655'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chaptersection',
            name='slug',
            field=models.SlugField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='coursechapter',
            name='slug',
            field=models.SlugField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='crashcourse',
            name='slug',
            field=models.SlugField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='sectioncontent',
            name='slug',
            field=models.SlugField(blank=True, max_length=128, null=True),
        ),
    ]
