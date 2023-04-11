# Generated by Django 4.1.7 on 2023-04-10 20:12

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("store", "0011_remove_product_inventory"),
    ]

    operations = [
        migrations.CreateModel(
            name="ColorInventory",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("quantity", models.IntegerField(blank=True, default=0)),
                (
                    "extra_price",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=6, null=True
                    ),
                ),
                (
                    "color",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="product_color",
                        to="store.colour",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Product Color & Inventories",
            },
        ),
        migrations.CreateModel(
            name="SizeInventory",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("quantity", models.IntegerField(blank=True, default=0)),
                (
                    "extra_price",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=6, null=True
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Product Size & Inventories",
            },
        ),
        migrations.AddField(
            model_name="product",
            name="inventory",
            field=models.IntegerField(
                default=1, validators=[django.core.validators.MinValueValidator(0)]
            ),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name="ProductColorSizeInventory",
        ),
        migrations.AddField(
            model_name="sizeinventory",
            name="product",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="size_inventory",
                to="store.product",
            ),
        ),
        migrations.AddField(
            model_name="sizeinventory",
            name="size",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="product_size",
                to="store.size",
            ),
        ),
        migrations.AddField(
            model_name="colorinventory",
            name="product",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="color_inventory",
                to="store.product",
            ),
        ),
    ]
