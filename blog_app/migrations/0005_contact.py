# Generated by Django 4.1.4 on 2023-01-01 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog_app", "0004_newsletter_alter_post_category"),
    ]

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
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("message", models.TextField()),
                ("name", models.CharField(max_length=200)),
                ("email", models.EmailField(max_length=254)),
                ("subject", models.CharField(max_length=200)),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
