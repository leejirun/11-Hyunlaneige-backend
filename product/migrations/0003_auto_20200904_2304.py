# Generated by Django 3.0.8 on 2020-09-04 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20200904_2216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maincategory',
            name='name',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='product',
            name='english_name',
            field=models.CharField(max_length=256),
        ),
        migrations.AlterField(
            model_name='product',
            name='korean_name',
            field=models.CharField(max_length=256),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='name',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='tag',
            name='tag',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='typecategory',
            name='name',
            field=models.CharField(max_length=128),
        ),
    ]