# Generated by Django 3.0.6 on 2020-05-16 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skills', '0002_auto_20200516_1539'),
    ]

    operations = [
        migrations.AlterField(
            model_name='program_skill',
            name='title',
            field=models.CharField(max_length=150, verbose_name='Title'),
        ),
    ]
