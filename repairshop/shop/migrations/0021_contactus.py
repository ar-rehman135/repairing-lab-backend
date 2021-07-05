# Generated by Django 3.2.4 on 2021-07-05 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0020_mobilerepairing'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('contactId', models.AutoField(primary_key=True, serialize=False)),
                ('fullName', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100, unique=True)),
                ('subject', models.CharField(max_length=100)),
                ('phoneNO', models.CharField(max_length=50)),
                ('message', models.TextField(blank=True)),
            ],
        ),
    ]
