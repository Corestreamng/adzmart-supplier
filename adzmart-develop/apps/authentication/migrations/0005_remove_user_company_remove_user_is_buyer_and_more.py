# Generated by Django 4.0.5 on 2022-07-18 11:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0004_rename_user_supplier_owner_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='company',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_buyer',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_supplier',
        ),
        migrations.AddField(
            model_name='user',
            name='supplier',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='authentication.supplier'),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='owner',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='supplier_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
