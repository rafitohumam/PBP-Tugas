# Generated by Django 4.1 on 2022-09-21 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mywatchlist', '0003_rename_description_mywatchlist_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mywatchlist',
            name='rating',
            field=models.FloatField(),
        ),
    ]
