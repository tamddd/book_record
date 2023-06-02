# Generated by Django 4.1.7 on 2023-05-30 15:10

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="BookModel",
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
                ("title", models.CharField(max_length=60)),
                ("author", models.CharField(max_length=60)),
                ("reports", models.TextField()),
                ("purchase_date", models.DateField(auto_now=True)),
                ("finished_date", models.DateField(blank=True)),
                ("is_finished", models.BooleanField(default=False)),
                (
                    "category",
                    models.CharField(
                        choices=[
                            ("business", "ビジネス"),
                            ("computer", "コンピュータ"),
                            ("other", "その他"),
                        ],
                        max_length=100,
                    ),
                ),
            ],
        ),
    ]
