# Generated by Django 5.1 on 2024-10-07 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beposoft_app', '0021_remove_singleproducts_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='family',
            field=models.ManyToManyField(related_name='familys', to='beposoft_app.family'),
        ),
    ]
