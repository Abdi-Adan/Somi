# Generated by Django 2.1.7 on 2019-03-17 01:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Notes', '0002_auto_20190314_0031'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='note_slug',
            field=models.SlugField(null=True),
        ),
    ]
