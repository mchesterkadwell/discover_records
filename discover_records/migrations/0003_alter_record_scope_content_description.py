# Generated by Django 4.1.9 on 2023-05-08 18:33

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("discover_records", "0002_remove_record_id_alter_record_record_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="record",
            name="scope_content_description",
            field=models.CharField(blank=True, max_length=250),
        ),
    ]
