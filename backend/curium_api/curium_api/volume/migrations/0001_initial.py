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
            name="VolumeRecord",
            fields=[
                (
                    "record_id",
                    models.UUIDField(
                        auto_created=True,
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("upload_date", models.DateTimeField(auto_now_add=True)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("UPLOADED", "Uploaded"),
                            ("QUEUED", "Queued"),
                            ("PROCESSING", "Processing"),
                            ("INTERMEDIATE_STATE", "Intermediate State"),
                            ("COMPLETED", "Completed"),
                        ],
                        max_length=20,
                    ),
                ),
                ("patient_id", models.CharField(max_length=255)),
                ("study_id", models.CharField(max_length=255)),
                ("volume_meta", models.JSONField(blank=True, null=True)),
                ("report_meta", models.JSONField(blank=True, null=True)),
                ("isAutomated", models.BooleanField(default=False)),
                (
                    "org",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="organization.organization",
                    ),
                ),
                (
                    "uploaded_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
