# Generated by Django 2.0.1 on 2018-01-24 14:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gameshop', '0011_developer_studioname'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='developer',
            name='studioname',
        ),
    ]