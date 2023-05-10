# Generated by Django 4.1.7 on 2023-05-10 22:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("store", "0024_alter_order_transaction_ref"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cart",
            name="customer",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="carts",
                to=settings.AUTH_USER_MODEL,
                unique=True,
            ),
        ),
        migrations.AlterField(
            model_name="order",
            name="transaction_ref",
            field=models.CharField(max_length=32, unique=True),
        ),
    ]
