# Generated by Django 3.2.6 on 2021-10-19 09:29

import logging
import time
from datetime import timedelta

from django.core.cache import cache
from django.db import migrations
from django.utils import timezone

from ureport.utils import chunk_list

logger = logging.getLogger(__name__)


def noop(apps, schema_editor):  # pragma: no cover
    pass


def populate_contact_activities_used(apps, schema_editor):  # pragma: no cover
    Org = apps.get_model("orgs", "Org")
    ContactActivity = apps.get_model("stats", "ContactActivity")

    today = timezone.now().date()

    # We'll be indexing the objects newer than 400 days, around 1 months
    start = today - timedelta(days=400)

    orgs = Org.objects.all().order_by("id")

    for org in orgs:
        start_time = time.time()

        print(f"Migrating contact_activities on org #{org.id}")

        contact_activities_used_max_id_key = f"contact_activities_used_max_id:{org.id}"
        max_id = cache.get(contact_activities_used_max_id_key, 0)

        contact_activities_ids = (
            ContactActivity.objects.filter(org=org, date__gte=start, id__gt=max_id)
            .order_by("id")
            .values_list("id", flat=True)
        )

        org_count = 0

        for batch in chunk_list(contact_activities_ids, 1000):
            batch_ids = list(batch)
            latest_id = batch_ids[-1]

            updated = ContactActivity.objects.filter(id__in=batch_ids).update(used=True)

            org_count += updated

            elapsed = time.time() - start_time
            logger.info(
                f"Populating used on {org_count} contacts activities for org #{org.id} in {elapsed:.1f} seconds"
            )

            cache.set(contact_activities_used_max_id_key, latest_id, None)

        logger.info(
            f"Finished populating used on {org_count} contacts activities for org #{org.id} in {elapsed:.1f} seconds"
        )


def apply_manual():  # pragma: no cover
    from django.apps import apps

    populate_contact_activities_used(apps, None)


class Migration(migrations.Migration):

    dependencies = [
        ("stats", "0019_contactactivity_used"),
    ]

    operations = [migrations.RunPython(populate_contact_activities_used, noop)]
