# Generated by Django 5.1.5 on 2025-01-28 11:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_tags_recipe_tags'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Tags',
            new_name='Tag',
        ),
    ]
