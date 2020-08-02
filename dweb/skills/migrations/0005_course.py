# Generated by Django 2.1.7 on 2020-06-30 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skills', '0004_project'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cw', models.CharField(max_length=250, verbose_name='Type')),
                ('title', models.CharField(max_length=150, verbose_name='Name')),
                ('description', models.TextField(verbose_name='Description')),
                ('source', models.CharField(max_length=250, verbose_name='From')),
                ('date', models.DateField()),
            ],
        ),
    ]