# Generated by Django 4.0.1 on 2022-01-16 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resource_search', '0005_format_resource_formats'),
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='resource',
            name='languages',
            field=models.ManyToManyField(to='resource_search.Language'),
        ),
    ]
