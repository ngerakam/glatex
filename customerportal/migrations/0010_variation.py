# Generated by Django 3.2.5 on 2021-10-07 03:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customerportal', '0009_rename_cart_mycart'),
    ]

    operations = [
        migrations.CreateModel(
            name='Variation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('variation_category', models.CharField(choices=[('color', 'color'), ('size', 'size')], max_length=100)),
                ('variation_value', models.CharField(max_length=100)),
                ('created_date', models.DateTimeField(auto_now=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customerportal.product')),
            ],
        ),
    ]
