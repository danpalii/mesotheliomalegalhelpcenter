# from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView

from .models import ArticlesModel, CategoryModel

class HomeView(TemplateView):
    template_name = 'content_manager/index.html'

class FaqView(TemplateView):
    template_name = 'content_manager/faq_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category_content = CategoryModel.objects.all()
        context['category_content'] = category_content

        return context


class CategoryView(TemplateView):
    template_name = 'content_manager/category_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        article_content = ArticlesModel.objects.filter(category__slug=self.kwargs.get('slug'))
        category_content = CategoryModel.objects.get(slug=self.kwargs.get('slug'))

        context['article_content'] = article_content
        context['category_content'] = category_content
        return context

class ArticleView(TemplateView):
    template_name = 'content_manager/article_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        article_content = ArticlesModel.objects.get(slug=self.kwargs.get('art_slug'))

        context['current_category'] = CategoryModel.objects.get(slug=self.kwargs.get('cat_slug'))
        context['article_content'] = article_content
        return context