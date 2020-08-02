# Generated by Django 2.1.7 on 2020-07-02 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skills', '0007_program_skill_logo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('org', models.CharField(max_length=250, verbose_name='Organization')),
                ('duration', models.CharField(max_length=150, verbose_name='Duration')),
                ('position', models.CharField(max_length=150, verbose_name='Position')),
                ('description', models.TextField(verbose_name='Description')),
                ('date', models.DateField()),
            ],
        ),
    ]