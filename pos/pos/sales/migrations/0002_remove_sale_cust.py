# Generated by Django 2.2 on 2020-09-18 06:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sale',
            name='cust',
        ),
    ]
