# Generated by Django 3.1.3 on 2021-02-01 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Device', '0002_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='images'),
        ),
    ]
