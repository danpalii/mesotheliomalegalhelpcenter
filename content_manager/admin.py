from django.contrib import admin
from django.http import HttpResponseRedirect
from django.shortcuts import reverse

from .models import (
    AuthorsModel, ArticlesModel, CategoryModel
    )
@admin.register(AuthorsModel)
class AuthorAdmin(admin.ModelAdmin):
    fields = ['author_name']

    list_display = ['author_name']
    list_display_links = ['author_name']

@admin.register(CategoryModel)
class CategoryAdmin(admin.ModelAdmin):
    fields = ['category_name', 'slug', 'snippet', 'category_feature_image',]

    list_display = ['category_name']
    list_display_links = ['category_name']
    prepopulated_fields = {'slug': ('category_name',)}

@admin.register(ArticlesModel)
class ArticlesAdmin(admin.ModelAdmin):
    fieldsets = (
        ('', {'fields': (
                           'name', 'slug', 'category', 'meta_title',
                           'meta_description', 'meta_reading_time', 'snippet',
                           'feature_image', 'article'
        )}),
        ('', {'fields': ('author', 'related_articles', 'sort_number', 'dropdown_select')}),
        ('', {'fields': ('added_time', 'updated_time')}),
    )

    list_display = ['name', 'slug', 'added_time', 'updated_time','dropdown_select']
    list_display_links = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ('category',)
    readonly_fields = (
        'added_time',
        'updated_time',
    )


    def response_change(self, request, obj):
        ret = super().response_change(request, obj)
        if '_preview' in request.POST:
            return HttpResponseRedirect(reverse('article', kwargs={'cat_slug': obj.category.slug, 'art_slug': obj.slug}))
        return ret

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == "related_articles":
            if 'object_id' in request.resolver_match.kwargs:
                kwargs["queryset"] = ArticlesModel.objects.exclude(id=request.resolver_match.kwargs['object_id'])
            else:
                kwargs["queryset"] = ArticlesModel.objects.all()
        return super(ArticlesAdmin, self).formfield_for_manytomany(db_field, request, **kwargs)