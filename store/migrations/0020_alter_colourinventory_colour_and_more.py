# Generated by Django 4.1.7 on 2023-04-19 20:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("store", "0019_alter_colourinventory_colour_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="colourinventory",
            name="colour",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="product_color",
                to="store.colour",
            ),
        ),
        migrations.AlterField(
            model_name="sizeinventory",
            name="size",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="product_size",
                to="store.size",
            ),
        ),
    ]
