# Generated by Django 3.2.4 on 2021-07-09 14:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0023_auto_20210709_1714'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='LaptopRepairing',
            new_name='Repairing',
        ),
        migrations.DeleteModel(
            name='MobileRepairing',
        ),
    ]
