# Generated by Django 5.1 on 2024-10-04 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beposoft_app', '0020_alter_variantproducts_stock'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='singleproducts',
            name='price',
        ),
        migrations.RemoveField(
            model_name='singleproducts',
            name='stock',
        ),
        migrations.AddField(
            model_name='products',
            name='stock',
            field=models.IntegerField(default=0),
        ),
    ]