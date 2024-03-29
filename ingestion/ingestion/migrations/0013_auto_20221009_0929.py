# Generated by Django 3.2.9 on 2022-10-09 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ingestion', '0012_auto_20220820_0432'),
    ]

    operations = [
        migrations.RenameField(
            model_name='influencers',
            old_name='email',
            new_name='Email',
        ),
        migrations.RenameField(
            model_name='influencers',
            old_name='email1',
            new_name='Email1',
        ),
        migrations.RenameField(
            model_name='influencers',
            old_name='email2',
            new_name='Email2',
        ),
        migrations.RenameField(
            model_name='photographerleads',
            old_name='name',
            new_name='Name',
        ),
        migrations.RenameField(
            model_name='photographerleads',
            old_name='pro',
            new_name='Pro',
        ),
        migrations.RenameField(
            model_name='photographerleads',
            old_name='productowned',
            new_name='ProductOwned',
        ),
        migrations.RenameField(
            model_name='photographerleads',
            old_name='salesperson',
            new_name='SalesPerson',
        ),
        migrations.RenameField(
            model_name='photographerleads',
            old_name='website',
            new_name='Website',
        ),
        migrations.AlterField(
            model_name='eventregistration',
            name='Country',
            field=models.CharField(choices=[('IND', 'INDIA'), ('MAL', 'Malaysia')], default='IND', help_text='Country', max_length=100),
        ),
        migrations.AlterField(
            model_name='eventregistration',
            name='PermissionToShareData',
            field=models.BooleanField(default='True', help_text='Whether the attender has given permission to share data'),
        ),
        migrations.AlterField(
            model_name='eventregistration',
            name='Photographer',
            field=models.BooleanField(default='True', help_text='Whether attender is a photographer or not'),
        ),
        migrations.AlterField(
            model_name='eventregistration',
            name='Pro',
            field=models.BooleanField(default='True', help_text='Whether the photographer is a pro or not'),
        ),
        migrations.AlterField(
            model_name='events',
            name='Country',
            field=models.CharField(choices=[('IND', 'INDIA'), ('MAL', 'Malaysia')], default='IND', help_text='Country', max_length=100),
        ),
        migrations.AlterField(
            model_name='influencers',
            name='Country',
            field=models.CharField(choices=[('IND', 'INDIA'), ('MAL', 'Malaysia')], default='IND', max_length=100),
        ),
        migrations.AlterField(
            model_name='influencers',
            name='GenreTags',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='institutionalclients',
            name='Country',
            field=models.CharField(choices=[('IND', 'INDIA'), ('MAL', 'Malaysia')], default='IND', max_length=100),
        ),
        migrations.AlterField(
            model_name='photographerleads',
            name='Country',
            field=models.CharField(choices=[('IND', 'INDIA'), ('MAL', 'Malaysia')], default='IND', help_text='Country', max_length=100),
        ),
        migrations.AlterField(
            model_name='servicerequests',
            name='Country',
            field=models.CharField(choices=[('IND', 'INDIA'), ('MAL', 'Malaysia')], default='IND', max_length=100),
        ),
        migrations.AlterField(
            model_name='servicerequests',
            name='ResolvedBy',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='socialmediaenquiries',
            name='Country',
            field=models.CharField(choices=[('IND', 'INDIA'), ('MAL', 'Malaysia')], default='IND', max_length=100),
        ),
    ]
