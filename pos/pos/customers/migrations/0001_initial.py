# Generated by Django 2.2 on 2020-09-17 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cust',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(default='')),
                ('gender', models.TextField(default='')),
                ('phone', models.TextField(default='')),
                ('addrs', models.TextField(default='')),
            ],
        ),
    ]
