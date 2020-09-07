# Generated by Django 3.0.8 on 2020-09-05 13:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_auto_20200904_2305'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='htmltag',
            name='product',
        ),
        migrations.RemoveField(
            model_name='image',
            name='product',
        ),
        migrations.RemoveField(
            model_name='ingredient',
            name='product',
        ),
        migrations.RemoveField(
            model_name='precaution',
            name='product',
        ),
        migrations.RemoveField(
            model_name='product',
            name='type_category',
        ),
        migrations.RemoveField(
            model_name='size',
            name='product',
        ),
        migrations.RemoveField(
            model_name='subcategory',
            name='main_category',
        ),
        migrations.RemoveField(
            model_name='tag',
            name='product',
        ),
        migrations.RemoveField(
            model_name='typecategory',
            name='sub_category',
        ),
        migrations.RemoveField(
            model_name='typecategoryproduct',
            name='product',
        ),
        migrations.RemoveField(
            model_name='typecategoryproduct',
            name='type_category',
        ),
        migrations.DeleteModel(
            name='Description',
        ),
        migrations.DeleteModel(
            name='HtmlTag',
        ),
        migrations.DeleteModel(
            name='Image',
        ),
        migrations.DeleteModel(
            name='Ingredient',
        ),
        migrations.DeleteModel(
            name='MainCategory',
        ),
        migrations.DeleteModel(
            name='Precaution',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.DeleteModel(
            name='Size',
        ),
        migrations.DeleteModel(
            name='SubCategory',
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
        migrations.DeleteModel(
            name='TypeCategory',
        ),
        migrations.DeleteModel(
            name='TypeCategoryProduct',
        ),
    ]
