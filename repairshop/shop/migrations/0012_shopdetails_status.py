# Generated by Django 3.2.4 on 2021-07-01 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0011_remove_shopdetails_isdeleted'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopdetails',
            name='status',
            field=models.BooleanField(default=False, null=True),
        ),
    ]