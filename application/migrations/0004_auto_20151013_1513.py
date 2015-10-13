# -*- coding: utf-8 -*-
# Generated by Django 1.9a1 on 2015-10-13 09:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0003_auto_20151006_1950'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='is_anonymous',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='application',
            name='privacy_policy',
            field=models.URLField(blank=True, help_text=b'Link of privacy policy of application', null=True),
        ),
        migrations.AddField(
            model_name='application',
            name='required_scopes',
            field=models.CharField(blank=True, help_text=b'Default non-tracking permissions. Valid only if application is anonymous', max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='application',
            name='website',
            field=models.URLField(blank=True, null=True),
        ),
    ]