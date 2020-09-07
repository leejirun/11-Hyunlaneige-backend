# Generated by Django 3.0.8 on 2020-09-04 22:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HtmlTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detail', models.URLField(max_length=2048, null=True)),
            ],
            options={
                'db_table': 'html_tags',
            },
        ),
        migrations.RenameField(
            model_name='product',
            old_name='name',
            new_name='korean_name',
        ),
        migrations.AddField(
            model_name='product',
            name='english_name',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.DeleteModel(
            name='Video',
        ),
        migrations.AddField(
            model_name='htmltag',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.Product'),
        ),
    ]
