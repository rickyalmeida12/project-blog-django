# Generated by Django 4.2.1 on 2023-06-08 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_post_created_by_post_updated_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
