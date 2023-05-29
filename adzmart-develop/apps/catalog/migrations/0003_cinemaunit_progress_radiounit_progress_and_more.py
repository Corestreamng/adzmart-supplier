# Generated by Django 4.0.5 on 2023-05-28 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_printunit_progress'),
    ]

    operations = [
        migrations.AddField(
            model_name='cinemaunit',
            name='progress',
            field=models.CharField(choices=[('Not Initiated', 'Not Initiated'), ('Processing', 'Processing'), ('Running', 'Running'), ('Complete', 'Complete'), ('Declined', 'Declined')], default='Not Initiated', max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='radiounit',
            name='progress',
            field=models.CharField(choices=[('Not Initiated', 'Not Initiated'), ('Processing', 'Processing'), ('Running', 'Running'), ('Complete', 'Complete'), ('Declined', 'Declined')], default='Not Initiated', max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='tvunit',
            name='progress',
            field=models.CharField(choices=[('Not Initiated', 'Not Initiated'), ('Processing', 'Processing'), ('Running', 'Running'), ('Complete', 'Complete'), ('Declined', 'Declined')], default='Not Initiated', max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='unit',
            name='progress',
            field=models.CharField(choices=[('Not Initiated', 'Not Initiated'), ('Processing', 'Processing'), ('Running', 'Running'), ('Complete', 'Complete'), ('Declined', 'Declined')], default='Not Initiated', max_length=30, null=True),
        ),
    ]
