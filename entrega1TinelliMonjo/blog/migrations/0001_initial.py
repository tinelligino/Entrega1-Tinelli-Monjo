# Generated by Django 4.1.1 on 2022-10-14 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Contact",
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
                ("asunto", models.CharField(max_length=50)),
                ("descripcion", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="Historia",
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
                ("resumen", models.CharField(max_length=50)),
                ("descripcion", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="User",
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
                ("nombre", models.CharField(max_length=50)),
                ("email", models.EmailField(max_length=254)),
                ("telefono", models.CharField(max_length=50)),
            ],
        ),
    ]
