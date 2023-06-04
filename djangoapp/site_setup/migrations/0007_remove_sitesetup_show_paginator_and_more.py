# Generated by Django 4.2.1 on 2023-06-04 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_setup', '0006_alter_sitesetup_favicon'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sitesetup',
            name='show_paginator',
        ),
        migrations.AddField(
            model_name='sitesetup',
            name='show_pagination',
            field=models.BooleanField(default=True),
        ),
    ]