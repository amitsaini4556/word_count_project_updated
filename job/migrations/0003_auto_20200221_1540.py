# Generated by Django 2.2.10 on 2020-02-21 10:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0002_auto_20200221_1535'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='counts',
            new_name='JOBS',
        ),
    ]