# Generated by Django 4.0.1 on 2022-01-18 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resource_search', '0006_language_resource_languages'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resource',
            name='year',
            field=models.CharField(blank=True, max_length=32),
        ),
    ]
