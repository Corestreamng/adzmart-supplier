# Generated by Django 4.0.5 on 2022-09-29 11:42

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0006_user_is_verified_alter_user_phone_no'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invitation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('phone_no', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Active', 'Active'), ('Rejected', 'Rejected')], default='Pending', max_length=50)),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.supplier')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]