# Generated by Django 4.1.4 on 2023-01-26 12:07

from django.db import migrations
import shortuuid.django_fields


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="account",
            name="id",
            field=shortuuid.django_fields.ShortUUIDField(
                alphabet=None,
                length=22,
                max_length=15,
                prefix="id_",
                primary_key=True,
                serialize=False,
            ),
        ),
    ]
