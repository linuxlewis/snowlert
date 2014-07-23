# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('data', jsonfield.fields.JSONField()),
                ('location', django.contrib.gis.db.models.fields.PointField(null=True, srid=4326, blank=True)),
                ('station_source', models.CharField(default='NOAA', max_length=4, choices=[('NOAA', 'National Oceanic and Atmospheric Administration'), ('OPNW', 'OpenWeather')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
