# Generated by Django 3.1.4 on 2021-01-17 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CustomerID', models.IntegerField()),
                ('CustomerName', models.TextField()),
                ('Gender', models.TextField()),
                ('pos_po', models.DecimalField(decimal_places=2, default=0.0, max_digits=19)),
                ('CLV', models.DecimalField(decimal_places=2, default=0.0, max_digits=19)),
            ],
        ),
        migrations.CreateModel(
            name='CustomerPurchaseInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CustomerID', models.IntegerField()),
                ('ProductID', models.IntegerField()),
                ('PurchaseQuantity', models.IntegerField()),
                ('PurchasePrice', models.IntegerField()),
                ('Comment', models.TextField()),
                ('Date', models.IntegerField()),
                ('pos_or_neg', models.DecimalField(decimal_places=2, default=0.0, max_digits=19)),
            ],
        ),
        migrations.CreateModel(
            name='MarketingIndex',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CustomerID', models.IntegerField()),
                ('ForecastPurchaseProb', models.DecimalField(decimal_places=2, default=0.0, max_digits=19)),
                ('CLV', models.DecimalField(decimal_places=2, default=0.0, max_digits=19)),
                ('WalletShare', models.DecimalField(decimal_places=2, default=0.0, max_digits=19)),
                ('CategoryDemandShare', models.DecimalField(decimal_places=2, default=0.0, max_digits=19)),
                ('ProportionofPositiveComment', models.DecimalField(decimal_places=2, default=0.0, max_digits=19)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ProductName', models.TextField()),
                ('InventoryAmount', models.IntegerField()),
                ('ProductID', models.IntegerField()),
                ('ProductPrice', models.DecimalField(decimal_places=2, default=0.0, max_digits=19)),
            ],
        ),
    ]
