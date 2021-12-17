# Generated by Django 3.2.5 on 2021-12-14 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customerportal', '0015_productimages'),
    ]

    operations = [
        migrations.AddField(
            model_name='productimages',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='customerportal/uploaded/products'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='customerportal/uploaded/products'),
        ),
    ]
