# Generated by Django 4.0.5 on 2023-05-30 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_cinemaunit_progress_radiounit_progress_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cinemaunit',
            name='total_duration',
            field=models.FloatField(default=1, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='printunit',
            name='total_duration',
            field=models.FloatField(default=1, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='radiounit',
            name='total_duration',
            field=models.FloatField(default=1, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='tvunit',
            name='total_duration',
            field=models.FloatField(default=1, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='unit',
            name='total_duration',
            field=models.FloatField(default=1, max_length=50, null=True),
        ),
    ]
