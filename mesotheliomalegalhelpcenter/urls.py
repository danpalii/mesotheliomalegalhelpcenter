from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from content_manager.views import HomeView, FaqView, CategoryView, ArticleView, upload_image

urlpatterns = [
    path('website-management/', admin.site.urls),
    path('', HomeView.as_view(), name='index'),
    path('faq/', FaqView.as_view(), name='faq'),
    path('faq/<slug:slug>', CategoryView.as_view(), name='category'),
    path('faq/<slug:cat_slug>/<slug:art_slug>', ArticleView.as_view(), name='article'),

    path("robots.txt", TemplateView.as_view(template_name="content_manager/robots.txt", content_type="text/plain")),  #add the robots.txt file
    path('tinymce/', include('tinymce.urls')),
    path('upload_image/', upload_image),

]
if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)