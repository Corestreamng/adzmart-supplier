# Generated by Django 4.1 on 2022-09-15 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("DFM", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="mediaadvisory",
            name="status",
            field=models.CharField(
                choices=[
                    ("Opened", "Opened"),
                    ("Processing", "Processing"),
                    ("Completed", "Completed"),
                ],
                default="Opened",
                max_length=50,
            ),
        ),
        migrations.AddField(
            model_name="mediabrief",
            name="status",
            field=models.CharField(
                choices=[
                    ("Opened", "Opened"),
                    ("Processing", "Processing"),
                    ("Completed", "Completed"),
                ],
                default="Opened",
                max_length=50,
            ),
        ),
        migrations.AddField(
            model_name="support",
            name="status",
            field=models.CharField(
                choices=[
                    ("Opened", "Opened"),
                    ("Processing", "Processing"),
                    ("Completed", "Completed"),
                ],
                default="Opened",
                max_length=50,
            ),
        ),
    ]