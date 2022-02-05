# Generated by Django 3.2.5 on 2021-12-10 15:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_portofolio_porto_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portofolio',
            name='porto_cat_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='portfolios', to='blog.portofolio_cat'),
        ),
    ]