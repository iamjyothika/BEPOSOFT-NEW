# Generated by Django 5.1 on 2024-10-26 07:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beposoft_app', '0039_order_family'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='state',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='beposoft_app.state'),
            preserve_default=False,
        ),
    ]