# Generated by Django 4.1.7 on 2023-05-10 21:25

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("store", "0023_alter_cartitem_options_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="transaction_ref",
            field=models.CharField(
                default="7DbEXR18VF-kA_lJ", max_length=12, unique=True
            ),
        ),
    ]
