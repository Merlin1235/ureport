# Generated by Django 2.2.12 on 2020-06-02 04:36

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("contacts", "0022_install_triggers"),
    ]

    operations = [
        migrations.AlterField(
            model_name="contact",
            name="uuid",
            field=models.CharField(max_length=36),
        ),
    ]
