# Generated by Django 2.2 on 2020-08-27 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='jenisobat',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='task',
            name='quantity',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='task',
            name='name',
            field=models.TextField(default=''),
        ),
    ]
