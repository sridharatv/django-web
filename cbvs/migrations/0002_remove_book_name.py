# Generated by Django 2.2.7 on 2019-12-03 15:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cbvs', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='name',
        ),
    ]
