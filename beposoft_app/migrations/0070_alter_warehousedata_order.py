# Generated by Django 5.0.6 on 2024-11-14 11:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beposoft_app', '0069_alter_warehousedata_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='warehousedata',
            name='order',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='warehouse_orders', to='beposoft_app.order'),
            preserve_default=False,
        ),
    ]
