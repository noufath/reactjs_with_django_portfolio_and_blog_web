# Generated by Django 3.2.5 on 2021-12-14 10:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_alter_portofolio_porto_cat_id'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='portofolio_cat',
            options={'ordering': ['id'], 'verbose_name': 'Portofolio Category', 'verbose_name_plural': 'Portofolio Category'},
        ),
    ]