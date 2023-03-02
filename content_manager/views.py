from django.conf import settings
from django.http import JsonResponse
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView
import os

from .models import ArticlesModel, CategoryModel


class HomeView(TemplateView):
    template_name = 'content_manager/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['article_select'] = ArticlesModel.objects.all()

        return context


class FaqView(TemplateView):
    template_name = 'content_manager/faq_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category_content'] = CategoryModel.objects.all()

        return context

class CategoryView(TemplateView):
    template_name = 'content_manager/category_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['category_content'] = CategoryModel.objects.get(slug=self.kwargs.get('slug'))
        context['article_content'] = ArticlesModel.objects.filter(category__slug
                                                                  =self.kwargs.get('slug')).order_by('sort_number')

        return context


class ArticleView(TemplateView):
    template_name = 'content_manager/article_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['current_category'] = CategoryModel.objects.get(slug=self.kwargs.get('cat_slug'))
        context['article_content'] = ArticlesModel.objects.get(slug=self.kwargs.get('art_slug'))
        context['category'] = CategoryModel.objects.all()

        return context


@csrf_exempt
def upload_image(request):
    if request.method == "POST":
        file_obj = request.FILES['file']
        file_name_suffix = file_obj.name.split(".")[-1]
        if file_name_suffix not in ["jpg", "png", "gif", "jpeg", ]:
            return JsonResponse({"message": "Wrong file format"})

        upload_time = timezone.now()
        path = os.path.join(
            settings.MEDIA_ROOT,
            'article_images',
            str(upload_time.year),
            str(upload_time.month),
            str(upload_time.day)
        )
        # If there is no such path, create
        if not os.path.exists(path):
            os.makedirs(path)

        file_path = os.path.join(path, file_obj.name)

        file_url = f'{settings.MEDIA_URL}article_images/{upload_time.year}/{upload_time.month}/{upload_time.day}/{file_obj.name}'

        if os.path.exists(file_path):
            return JsonResponse({
                "message": "file already exist",
                'location': file_url
            })

        with open(file_path, 'wb+') as f:
            for chunk in file_obj.chunks():
                f.write(chunk)

        return JsonResponse({
            'message': 'Image uploaded successfully',
            'location': file_url
        })
    return JsonResponse({'detail': "Wrong request"})