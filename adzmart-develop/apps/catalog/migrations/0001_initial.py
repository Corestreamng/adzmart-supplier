# Generated by Django 4.0.5 on 2023-05-22 12:08

import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BillboardImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('reference_id', models.CharField(blank=True, max_length=255, null=True)),
                ('image_public_id', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UnitType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(blank=True, max_length=50, null=True, unique=True)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('supplier', models.CharField(blank=True, max_length=50, null=True)),
                ('display_name', models.CharField(blank=True, max_length=50, null=True)),
                ('adzmart_hash', models.CharField(blank=True, default=None, max_length=64, null=True, unique=True)),
                ('reference_id', models.CharField(blank=True, max_length=200, null=True, unique=True, verbose_name='Reference ID')),
                ('billboard_id', models.CharField(blank=True, max_length=200, null=True, unique=True, verbose_name='Billboard ID')),
                ('latitude', models.FloatField(blank=True, null=True)),
                ('longitude', models.FloatField(blank=True, null=True)),
                ('district', models.CharField(blank=True, max_length=255, null=True)),
                ('state', models.CharField(blank=True, max_length=255, null=True)),
                ('postal_code', models.CharField(blank=True, max_length=100, null=True)),
                ('country', models.CharField(blank=True, max_length=100, null=True)),
                ('facing', models.CharField(choices=[('N', 'North'), ('S', 'South'), ('E', 'East'), ('W', 'West'), ('NE', 'North East'), ('NW', 'North West'), ('SE', 'South East'), ('SW', 'South West')], max_length=2, null=True)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('unit_info', models.JSONField(blank=True, null=True)),
                ('total', models.FloatField(default=0.0)),
                ('unit_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.unittype')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TVUnit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('Mp_Code', models.IntegerField(blank=True, null=True)),
                ('Vendor_Name', models.CharField(blank=True, max_length=255, null=True)),
                ('Corporate_Name', models.CharField(blank=True, max_length=255, null=True)),
                ('Station_Name', models.CharField(blank=True, max_length=255, null=True)),
                ('State', models.CharField(blank=True, max_length=255, null=True)),
                ('Media_Type', models.CharField(default='TV', max_length=255, null=True)),
                ('Rate_Desc', models.CharField(blank=True, max_length=255, null=True)),
                ('Time', models.CharField(blank=True, help_text='e.g. 6:00am-7:00am. You can separate multiple times using comma', max_length=255, null=True)),
                ('Duration', models.CharField(blank=True, help_text='e.g. 10secs', max_length=255, null=True)),
                ('Card_Rate', models.CharField(blank=True, max_length=255, null=True)),
                ('Nego_Rate', models.CharField(blank=True, max_length=255, null=True)),
                ('Nego_SC', models.CharField(blank=True, max_length=255, null=True)),
                ('Card_SC', models.CharField(blank=True, max_length=255, null=True)),
                ('Card_VD', models.IntegerField(blank=True, default=15, null=True)),
                ('Nego_VD', models.IntegerField(blank=True, null=True)),
                ('Add_VD', models.IntegerField(blank=True, null=True)),
                ('SP_Disc', models.CharField(blank=True, max_length=255, null=True)),
                ('Agency', models.IntegerField(blank=True, null=True)),
                ('VAT', models.FloatField(blank=True, default=7.5, null=True)),
                ('Mon', models.CharField(blank=True, default='Y', max_length=50, null=True)),
                ('Tue', models.CharField(blank=True, default='Y', max_length=50, null=True)),
                ('Wed', models.CharField(blank=True, default='Y', max_length=50, null=True)),
                ('Thur', models.CharField(blank=True, default='Y', max_length=50, null=True)),
                ('Fri', models.CharField(blank=True, default='Y', max_length=50, null=True)),
                ('Sat', models.CharField(blank=True, default='Y', max_length=50, null=True)),
                ('Sun', models.CharField(blank=True, default='Y', max_length=50, null=True)),
                ('total', models.FloatField(default=0.0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tv_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SpecialOffers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(help_text='Title of special offer campaign. e.g Online Banner Package', max_length=100, null=True)),
                ('description', models.TextField(help_text='Enter a detailed description of what the offer entails.', null=True)),
                ('services', models.TextField(help_text='Enter the included services for this offer', null=True)),
                ('rate', models.DecimalField(decimal_places=2, max_digits=10)),
                ('image', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='special_offer_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Special Offers',
            },
        ),
        migrations.CreateModel(
            name='RadioUnit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('Mp_Code', models.IntegerField(blank=True, null=True)),
                ('Vendor_Name', models.CharField(blank=True, max_length=255, null=True)),
                ('Corporate_Name', models.CharField(blank=True, max_length=255, null=True)),
                ('Station_Name', models.CharField(blank=True, max_length=255, null=True)),
                ('State', models.CharField(blank=True, max_length=255, null=True)),
                ('Media_Type', models.CharField(default='RD', max_length=255, null=True)),
                ('Rate_Desc', models.CharField(blank=True, max_length=255, null=True)),
                ('Time', models.CharField(blank=True, help_text='e.g. 6:00am-7:00am. You can separate multiple times using comma', max_length=255, null=True)),
                ('Duration', models.CharField(blank=True, help_text='e.g. 10secs', max_length=255, null=True)),
                ('Card_Rate', models.CharField(blank=True, max_length=255, null=True)),
                ('Nego_Rate', models.CharField(blank=True, max_length=255, null=True)),
                ('Nego_SC', models.CharField(blank=True, max_length=255, null=True)),
                ('Card_SC', models.CharField(blank=True, max_length=255, null=True)),
                ('Card_VD', models.IntegerField(blank=True, default=15, null=True)),
                ('Nego_VD', models.IntegerField(blank=True, null=True)),
                ('Add_VD', models.IntegerField(blank=True, null=True)),
                ('SP_Disc', models.CharField(blank=True, max_length=255, null=True)),
                ('Agency', models.IntegerField(blank=True, null=True)),
                ('VAT', models.FloatField(blank=True, default=7.5, null=True)),
                ('Mon', models.CharField(blank=True, default='Y', max_length=50, null=True)),
                ('Tue', models.CharField(blank=True, default='Y', max_length=50, null=True)),
                ('Wed', models.CharField(blank=True, default='Y', max_length=50, null=True)),
                ('Thur', models.CharField(blank=True, default='Y', max_length=50, null=True)),
                ('Fri', models.CharField(blank=True, default='Y', max_length=50, null=True)),
                ('Sat', models.CharField(blank=True, default='Y', max_length=50, null=True)),
                ('Sun', models.CharField(blank=True, default='Y', max_length=50, null=True)),
                ('total', models.FloatField(default=0.0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='radio_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PrintUnit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('coverage', models.CharField(choices=[('National', 'National'), ('North East', 'North East'), ('North West', 'North West'), ('North Central', 'North Central'), ('South East', 'South East'), ('South West', 'South West'), ('South South', 'South South')], max_length=20, null=True)),
                ('publisher', models.CharField(blank=True, max_length=100, null=True)),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('type', models.CharField(choices=[('Color', 'Color'), ('Black and White', 'Black and White')], max_length=15, null=True)),
                ('size', models.CharField(blank=True, max_length=50, null=True)),
                ('position', models.CharField(blank=True, max_length=150, null=True)),
                ('rate', models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True)),
                ('agency_discount', models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True)),
                ('amount', models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True)),
                ('vat', models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True)),
                ('total', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='print_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CinemaUnit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('cinema', models.CharField(blank=True, max_length=100, null=True)),
                ('location', models.CharField(blank=True, max_length=255, null=True)),
                ('rate_per_spot', models.IntegerField(blank=True, null=True)),
                ('state', models.CharField(blank=True, max_length=50, null=True)),
                ('total', models.FloatField(default=0.0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cinema_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddIndex(
            model_name='billboardimage',
            index=models.Index(fields=['image_public_id'], name='image_public_id_idx'),
        ),
    ]