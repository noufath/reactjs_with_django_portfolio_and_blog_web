# Generated by Django 3.2.5 on 2021-11-22 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20211122_0712'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='work_desc',
            field=models.TextField(blank=True, default=None),
        ),
    ]
