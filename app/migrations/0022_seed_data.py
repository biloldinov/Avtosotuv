from django.db import migrations
from django.core.management import call_command


def seed_data(apps, schema_editor):
    call_command('seed_data')


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0021_notification'),
    ]

    operations = [
        migrations.RunPython(seed_data, migrations.RunPython.noop),
    ]
