# Generated by Django 2.1.1 on 2019-04-07 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('communities', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='community',
            name='members',
            field=models.TextField(blank=True, null=True),
        ),
    ]
