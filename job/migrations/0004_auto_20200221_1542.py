# Generated by Django 2.2.10 on 2020-02-21 10:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0003_auto_20200221_1540'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='JOBS',
            new_name='Job',
        ),
    ]
