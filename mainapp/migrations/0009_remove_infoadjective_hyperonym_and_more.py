# Generated by Django 4.0.4 on 2022-05-31 04:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0008_infonoun_created_date_infonoun_updated_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='infoadjective',
            name='hyperonym',
        ),
        migrations.RemoveField(
            model_name='infoadjective',
            name='hyponym',
        ),
        migrations.DeleteModel(
            name='InfoNoun',
        ),
    ]
