# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('localities', '0018_auto_20160609_1255'),
    ]

    operations = [
        migrations.CreateModel(
            name='LocalityHealthsitesOSM',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('osm_id', models.BigIntegerField(db_index=True, null=True, blank=True)),
                ('osm_type', models.CharField(blank=True, max_length=30, null=True, choices=[(b'node', b'node'), (b'way', b'way'), (b'relation', b'relation')])),
                ('healthsite', models.OneToOneField(to='localities.Locality')),
            ],
            options={
                'ordering': ('healthsite__name',),
                'db_table': 'localities_healthsites_osm',
            },
        ),
    ]
