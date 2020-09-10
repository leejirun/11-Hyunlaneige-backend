# Generated by Django 3.0.8 on 2020-09-10 14:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0009_auto_20200908_1820'),
        ('user', '0009_auto_20200906_1734'),
    ]

    operations = [
        migrations.CreateModel(
            name='SkinType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skin_type', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'skin_types',
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.DecimalField(decimal_places=1, max_digits=2)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('comment', models.TextField()),
                ('review_image', models.URLField(blank=True, max_length=1024, null=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.Product')),
                ('skin_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='review.SkinType')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.User')),
            ],
            options={
                'db_table': 'reviews',
            },
        ),
    ]