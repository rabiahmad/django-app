# Generated by Django 3.2.18 on 2023-03-25 01:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_auto_20230324_2149'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('row_id', models.IntegerField()),
                ('order_id', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('order_date', models.DateField()),
                ('ship_date', models.DateField()),
                ('ship_mode', models.CharField(max_length=50)),
                ('customer_id', models.CharField(max_length=50)),
                ('customer_name', models.CharField(max_length=100)),
                ('segment', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('postal_code', models.IntegerField()),
                ('region', models.CharField(max_length=50)),
                ('product_id', models.CharField(max_length=50)),
                ('category', models.CharField(max_length=50)),
                ('sub_category', models.CharField(max_length=50)),
                ('product_name', models.CharField(max_length=200)),
                ('sales', models.FloatField()),
            ],
        ),
    ]
