# Generated by Django 3.2.9 on 2021-11-30 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ingestion', '0004_auto_20211125_0836'),
    ]

    operations = [
        migrations.AddField(
            model_name='contacts',
            name='category',
            field=models.CharField(default='Unknown', max_length=200),
        ),
        migrations.AddField(
            model_name='contacts',
            name='company_name',
            field=models.CharField(default='Unknown', max_length=200),
        ),
    ]
