# Generated by Django 5.0.4 on 2024-04-18 17:12

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("organization", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Membership",
            fields=[
                (
                    "membership_id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "role",
                    models.CharField(
                        choices=[
                            ("ADMIN", "Admin"),
                            ("SURGEON", "Surgeon"),
                            ("TELERADIOLOGIST", "Teleradiologist"),
                        ],
                        max_length=20,
                    ),
                ),
                (
                    "org",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="organization.organization",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
