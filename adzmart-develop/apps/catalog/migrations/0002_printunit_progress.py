# Generated by Django 4.0.5 on 2023-05-28 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='printunit',
            name='progress',
            field=models.CharField(choices=[('Not Initiated', 'Not Initiated'), ('Processing', 'Processing'), ('Running', 'Running'), ('Complete', 'Complete'), ('Declined', 'Declined')], default='Not Initiated', max_length=30, null=True),
        ),
    ]
