# Generated by Django 2.1.7 on 2020-07-01 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skills', '0006_certificate'),
    ]

    operations = [
        migrations.AddField(
            model_name='program_skill',
            name='logo',
            field=models.CharField(default='', max_length=250, verbose_name='img'),
        ),
    ]
