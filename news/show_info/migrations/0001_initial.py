# Generated by Django 4.2.7 on 2023-11-14 12:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Category name')),
            ],
        ),
        migrations.CreateModel(
            name='New',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('text', models.TextField(verbose_name='Text')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='news/%Y/%m/%d/', verbose_name='Photo')),
                ('date', models.DateField(auto_now_add=True, verbose_name='Date')),
                ('slug', models.SlugField(blank=True, max_length=255, null=True, unique=True, verbose_name='Slug')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='show_info.category', verbose_name='Category')),
            ],
        ),
    ]