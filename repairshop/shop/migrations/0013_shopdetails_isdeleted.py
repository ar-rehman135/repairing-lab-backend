# Generated by Django 3.2.4 on 2021-07-01 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0012_shopdetails_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopdetails',
            name='isdeleted',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
