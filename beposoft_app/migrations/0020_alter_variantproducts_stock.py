# Generated by Django 5.1 on 2024-10-04 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beposoft_app', '0019_alter_user_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='variantproducts',
            name='stock',
            field=models.PositiveBigIntegerField(default=0, null=True),
        ),
    ]
