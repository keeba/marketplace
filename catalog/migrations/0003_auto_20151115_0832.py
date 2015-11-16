# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_catalog_seller'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catalog',
            name='seller',
            field=models.ForeignKey(related_name='seller', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
