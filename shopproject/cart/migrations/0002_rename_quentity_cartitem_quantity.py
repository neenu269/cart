# Generated by Django 4.1.3 on 2023-01-10 06:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartitem',
            old_name='quentity',
            new_name='quantity',
        ),
    ]
