# Generated by Django 5.0.4 on 2025-01-05 00:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_storeitem_redeemedstoreitem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storeitem',
            name='provider',
            field=models.IntegerField(default=-1),
        ),
    ]