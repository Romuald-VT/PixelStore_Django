# Generated by Django 4.1.6 on 2023-05-02 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_account_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]
