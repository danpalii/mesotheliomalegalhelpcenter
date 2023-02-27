from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

class WebSiteGeneralSettingsModel(models.Model):
    pass

class WebSiteDesignAndStyleModel(models.Model):
    pass

class MainPagesModel(models.Model):
    pass

class AuthorsModel(models.Model):
    author_name = models.CharField(max_length=100, blank=True)

    class Meta:
        verbose_name = "Author"
        verbose_name_plural = "Author"

    def __str__(self):
        return self.author_name

class CategoryModel(models.Model):
    category_name = models.CharField(max_length=255, blank=True)
    slug = models.CharField(max_length=150, blank=True, unique=True, db_index=True, verbose_name='SLUG/URL')
    category_feature_image = models.ImageField(upload_to='category_feature_image', blank=True)
    snippet = models.TextField(blank=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Category"

    def __str__(self):
        return self.category_name
class ArticlesModel(models.Model):
    name = models.CharField(max_length=150, blank=True)
    slug = models.CharField(max_length=150, blank=True, unique=True, db_index=True, verbose_name='SLUG/URL')
    meta_title = models.CharField(max_length=150, blank=True)
    meta_description = models.TextField(blank=True)
    meta_reading_time = models.CharField(max_length=50, blank=True)
    snippet = models.TextField(blank=True)
    feature_image = models.ImageField(upload_to='article_feature_image', blank=True)
    # article = RichTextField(blank=True)
    article = RichTextUploadingField(blank=True)
    author = models.ForeignKey('AuthorsModel', on_delete=models.CASCADE, blank=True)

    faq_q1 = models.CharField(max_length=255, blank=True, verbose_name='FAQ Q1')
    faq_a1 = models.TextField(blank=True, verbose_name='FAQ A1')

    faq_q2 = models.CharField(max_length=255, blank=True, verbose_name='FAQ Q2')
    faq_a2 = models.TextField(blank=True, verbose_name='FAQ A2')

    faq_q3 = models.CharField(max_length=255, blank=True, verbose_name='FAQ Q3')
    faq_a3 = models.TextField(blank=True, verbose_name='FAQ A3')
    category = models.ForeignKey('CategoryModel', on_delete=models.CASCADE, blank=True)
    related_articles = models.ManyToManyField('self', blank=True, symmetrical=False)

    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Article"
        verbose_name_plural = "Article"

    def __str__(self):
        return self.slug
