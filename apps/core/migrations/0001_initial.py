# Generated by Django 4.2.3 on 2023-07-06 17:15

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="RecordsModel",
            fields=[
                (
                    "pkid",
                    models.BigAutoField(
                        editable=False, primary_key=True, serialize=False
                    ),
                ),
                (
                    "id",
                    models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("product_name", models.CharField(max_length=30)),
                ("product_description", models.TextField()),
                ("price", models.DecimalField(decimal_places=6, max_digits=56)),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
