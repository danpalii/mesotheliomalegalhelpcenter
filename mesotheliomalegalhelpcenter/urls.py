"""mesotheliomalegalhelpcenter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from content_manager.views import HomeView, FaqView, CategoryView, ArticleView

urlpatterns = [
    path('website-management/', admin.site.urls),
    path('', HomeView.as_view(), name='index'),
    path('faq/', FaqView.as_view(), name='faq'),
    path('faq/<slug:slug>', CategoryView.as_view(), name='category'),
    path('faq/<slug:cat_slug>/<slug:art_slug>', ArticleView.as_view(), name='article'),

    path("robots.txt", TemplateView.as_view(template_name="content_manager/robots.txt", content_type="text/plain")),  #add the robots.txt file
    path('ckeditor/', include('ckeditor_uploader.urls')),

]
if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)