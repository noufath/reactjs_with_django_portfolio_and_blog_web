# Generated by Django 3.2.5 on 2021-11-09 10:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_rename_cat_title_blogpost_cat_title_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='cat_title_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='post', to='blog.categories'),
        ),
    ]
