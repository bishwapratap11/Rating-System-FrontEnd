# Generated by Django 3.2.5 on 2021-07-08 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('saral', '0005_rename_src_new_source_vid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new',
            name='source_vid',
            field=models.CharField(max_length=2000),
        ),
    ]