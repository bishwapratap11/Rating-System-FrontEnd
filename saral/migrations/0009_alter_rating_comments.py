# Generated by Django 3.2.5 on 2021-07-09 01:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('saral', '0008_rating_rating_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='comments',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
    ]