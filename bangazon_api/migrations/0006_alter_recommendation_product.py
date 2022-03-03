# Generated by Django 3.2.10 on 2022-03-02 20:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bangazon_api', '0005_auto_20220302_2035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recommendation',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products_recommended', to='bangazon_api.product'),
        ),
    ]