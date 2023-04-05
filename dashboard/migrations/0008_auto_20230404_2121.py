# Generated by Django 3.2.18 on 2023-04-04 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0007_alter_transaction_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='transaction',
            options={'ordering': ('row_id',)},
        ),
        migrations.AlterField(
            model_name='transaction',
            name='order_id',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='row_id',
            field=models.IntegerField(default=None, primary_key=True, serialize=False),
        ),
    ]