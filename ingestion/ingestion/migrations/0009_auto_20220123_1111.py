# Generated by Django 3.2.9 on 2022-01-23 11:11

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ingestion', '0008_auto_20220123_1059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacts',
            name='contact_created_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 1, 23, 11, 11, 46, 49458, tzinfo=utc), help_text='Potential contact created date'),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='last_inbound_contact_date',
            field=models.DateField(blank=True, default=datetime.datetime(2022, 1, 23, 11, 11, 46, 49576, tzinfo=utc), help_text='last Inbound Sales contact date'),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='last_outbound_contact_date',
            field=models.DateField(blank=True, default=datetime.datetime(2022, 1, 23, 11, 11, 46, 49593, tzinfo=utc), help_text='last Outbound Sales contact date'),
        ),
        migrations.AlterField(
            model_name='leads',
            name='lead_created_date',
            field=models.DateField(blank=True, default=datetime.datetime(2022, 1, 23, 11, 11, 46, 52219, tzinfo=utc), help_text='Lead Creation Date'),
        ),
    ]
