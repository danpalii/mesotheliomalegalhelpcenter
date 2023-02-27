# Generated by Django 3.2 on 2023-02-23 11:46

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthorsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_name', models.CharField(blank=True, max_length=100)),
            ],
            options={
                'verbose_name': 'Author',
                'verbose_name_plural': 'Author',
            },
        ),
        migrations.CreateModel(
            name='CategoryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(blank=True, max_length=255)),
                ('slug', models.CharField(blank=True, db_index=True, max_length=150, unique=True, verbose_name='SLUG/URL')),
                ('category_feature_image', models.ImageField(blank=True, upload_to='category_feature_image')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Category',
            },
        ),
        migrations.CreateModel(
            name='MainPagesModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='WebSiteDesignAndStyleModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='WebSiteGeneralSettingsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='ArticlesModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=150)),
                ('slug', models.CharField(blank=True, db_index=True, max_length=150, unique=True, verbose_name='SLUG/URL')),
                ('meta_title', models.CharField(blank=True, max_length=150)),
                ('meta_description', models.TextField(blank=True)),
                ('meta_reading_time', models.CharField(blank=True, max_length=50)),
                ('snippet', models.TextField(blank=True)),
                ('feature_image', models.ImageField(blank=True, upload_to='article_feature_image')),
                ('article', ckeditor.fields.RichTextField(blank=True)),
                ('faq_q1', models.CharField(blank=True, max_length=255, verbose_name='FAQ Q1')),
                ('faq_a1', models.TextField(blank=True, verbose_name='FAQ A1')),
                ('faq_q2', models.CharField(blank=True, max_length=255, verbose_name='FAQ Q2')),
                ('faq_a2', models.TextField(blank=True, verbose_name='FAQ A2')),
                ('faq_q3', models.CharField(blank=True, max_length=255, verbose_name='FAQ Q3')),
                ('faq_a3', models.TextField(blank=True, verbose_name='FAQ A3')),
                ('author', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='content_manager.authorsmodel')),
                ('category', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='content_manager.categorymodel')),
                ('related_articles', models.ManyToManyField(blank=True, to='content_manager.ArticlesModel')),
            ],
            options={
                'verbose_name': 'Article',
                'verbose_name_plural': 'Article',
            },
        ),
    ]
