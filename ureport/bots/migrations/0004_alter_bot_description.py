# Generated by Django 3.2.6 on 2021-10-13 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bots", "0003_auto_20211013_1306"),
    ]

    operations = [
        migrations.AlterField(
            model_name="bot",
            name="description",
            field=models.TextField(default="", help_text="A short description for this bot, required", max_length=320),
        ),
    ]