# Generated by Django 4.1.2 on 2023-02-17 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="FormData",
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
                ("name", models.CharField(max_length=255)),
                ("email", models.CharField(max_length=255)),
                ("destination", models.CharField(max_length=255)),
                ("number_of_travellers", models.IntegerField()),
                ("budget_per_person", models.IntegerField()),
            ],
        ),
        migrations.AddIndex(
            model_name="formdata",
            index=models.Index(fields=["name"], name="forms_formd_name_2b3ba7_idx"),
        ),
        migrations.AddIndex(
            model_name="formdata",
            index=models.Index(fields=["email"], name="forms_formd_email_ec8145_idx"),
        ),
        migrations.AddIndex(
            model_name="formdata",
            index=models.Index(
                fields=["destination"], name="forms_formd_destina_245751_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="formdata",
            index=models.Index(
                fields=["number_of_travellers"], name="forms_formd_number__2bd2b5_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="formdata",
            index=models.Index(
                fields=["budget_per_person"], name="forms_formd_budget__9189bb_idx"
            ),
        ),
    ]
