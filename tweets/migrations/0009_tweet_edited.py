# Generated by Django 3.2.4 on 2021-07-28 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0008_auto_20210725_2358'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweet',
            name='edited',
            field=models.BooleanField(default=False),
        ),
    ]
