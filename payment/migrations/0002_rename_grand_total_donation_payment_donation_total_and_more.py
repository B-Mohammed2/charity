# Generated by Django 4.2.5 on 2023-09-23 18:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='donation_payment',
            old_name='grand_total',
            new_name='donation_total',
        ),
        migrations.RemoveField(
            model_name='donation_payment',
            name='order_total',
        ),
    ]
