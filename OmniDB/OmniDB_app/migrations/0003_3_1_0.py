# Generated by Django 3.1.1 on 2020-11-06 13:43

from django.db import migrations


def populate_technologies(apps, schema_editor):
    Technology = apps.get_model('OmniDB_app', 'Technology')
    Technology(name='sqlite').save()


class Migration(migrations.Migration):

    dependencies = [
        ('OmniDB_app', '0002_3_0_1'),
    ]

    operations = [
        migrations.RunPython(
            code=populate_technologies,
        )
    ]
