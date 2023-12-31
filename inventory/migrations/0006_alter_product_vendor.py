# Generated by Django 4.2.3 on 2023-07-07 12:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vendors', '0001_initial'),
        ('inventory', '0005_alter_product_vendor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='vendor',
            field=models.ForeignKey(default=100, on_delete=django.db.models.deletion.CASCADE, to='vendors.vendor'),
            preserve_default=False,
        ),
    ]
