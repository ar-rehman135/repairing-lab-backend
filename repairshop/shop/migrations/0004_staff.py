# Generated by Django 3.2.4 on 2021-06-30 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_chooseus'),
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('StaffID', models.AutoField(primary_key=True, serialize=False)),
                ('staffimage', models.ImageField(default='', upload_to='images/')),
                ('StaffName', models.CharField(max_length=50)),
                ('Staffdesignation', models.CharField(max_length=50)),
                ('staffdetail', models.TextField(blank=True)),
            ],
        ),
    ]
