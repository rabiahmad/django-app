# Generated by Django 3.2.18 on 2023-04-03 20:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0006_auto_20230403_2149'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='transaction',
            options={'ordering': ('order_date', 'ship_date')},
        ),
    ]
