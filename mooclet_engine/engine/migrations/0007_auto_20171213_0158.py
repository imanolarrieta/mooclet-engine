# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-13 01:58


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('engine', '0006_auto_20171124_0744'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='value',
            index=models.Index(fields=['mooclet', 'learner', 'version'], name='engine_valu_mooclet_c50aaf_idx'),
        ),
    ]
