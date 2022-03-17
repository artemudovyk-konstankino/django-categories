# Generated by Django 3.0.6 on 2020-05-17 18:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("contenttypes", "0002_remove_content_type_name"),
        ("django_categories", "0003_auto_20200306_1050"),
    ]

    operations = [
        migrations.AlterField(
            model_name="categoryrelation",
            name="content_type",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="contenttypes.ContentType", verbose_name="content type"
            ),
        ),
    ]
