# Generated by Django 3.2.5 on 2021-11-04 07:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogpost',
            old_name='cat_title',
            new_name='cat_title_id',
        ),
    ]
