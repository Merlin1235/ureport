# Generated by Django 2.2.20 on 2021-07-16 18:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("flows", "0001_initial"),
        ("stats", "0010_add_index"),
    ]

    operations = [
        migrations.AddField(
            model_name="pollstats",
            name="flow_result",
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to="flows.FlowResult"),
        ),
        migrations.AddField(
            model_name="pollstats",
            name="flow_result_category",
            field=models.ForeignKey(
                null=True, on_delete=django.db.models.deletion.SET_NULL, to="flows.FlowResultCategory"
            ),
        ),
        migrations.AddField(
            model_name="pollwordcloud",
            name="flow_result",
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to="flows.FlowResult"),
        ),
    ]
