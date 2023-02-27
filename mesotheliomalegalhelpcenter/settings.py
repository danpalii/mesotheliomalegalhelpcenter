"""
Django settings for mesotheliomalegalhelpcenter project.

Generated by 'django-admin startproject' using Django 3.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import os
from decouple import config

BASE_DIR = Path(__file__).resolve().parent.parent

ENV = os.environ.get('ENV')
if int(os.environ.get('SECRET_KEY_VALUE', default=1)):
    SECRET_KEY = config('SECRET_KEY', cast=str)
else:
    SECRET_KEY = os.environ['SECRET_KEY']

DEBUG = int(os.environ.get("DEBUG", default=1))
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS').split(" ") if os.environ.get('ALLOWED_HOSTS') else ['localhost', '127.0.0.1']
ALLOWED_HOSTS = ['*']


INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'ckeditor',
    'ckeditor_uploader',
    'embed_video',

    'content_manager',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mesotheliomalegalhelpcenter.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'mesotheliomalegalhelpcenter.wsgi.application'

if int(os.environ.get('DATABASEUSE', default=1)):
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
else:
    DATABASES = {
      'default': {
        'HOST': os.environ['PMA_HOST'],
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'USER': os.environ['POSTGRES_USER'],
        'PASSWORD': os.environ['POSTGRES_PASSWORD'],
        'NAME': os.environ['POSTGRES_DB'],
      },
    }

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'
# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, 'static'),
# ]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

if int(os.environ['GAE_APPLICATION']):
    DEFAULT_FILE_STORAGE = 'storages.backends.gcloud.GoogleCloudStorage'
    GS_BUCKET_NAME = 'media_mesothelioma_how'
    GS_DEFAULT_ACL = 'publicRead'
    MEDIA_URL = 'https://storage.googleapis.com/media_mesothelioma_how/'
else:
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
    MEDIA_URL = '/media/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Admin Panel settings
JAZZMIN_SETTINGS = {
    "site_title": "Admin Panel",
    "search_model": ["content_manager.Articles",],
    "show_ui_builder": True,
    "related_modal_active": True,
    "custom_css": "jazzmin/css/custom_main.css",
    "custom_links": {
        "content_manager": [{
            # Any Name you like
            "name": "Preview",
            "url": "index",
            "permissions": ["auth"]
        }]
    },
}

JAZZMIN_UI_TWEAKS = {
    "theme": "simplex",
}


EMBED_VIDEO_BACKENDS = {
    'default': 'embed_video.backends.YoutubeBackend',
}
CKEDITOR_UPLOAD_PATH = "ckeditor_image/"
CKEDITOR_JQUERY_URL = '//ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js'


# CKEDITOR_CONFIGS = {
#     'default': {
#         'toolbar_Full': [
#             ['Styles', 'Format', 'Bold', 'Italic', 'Underline', 'Strike', 'SpellChecker', 'Undo', 'Redo'],
#             ['Link', 'Unlink', 'Anchor', 'Iframe', 'Embed'],
#             ['Image','Image2', 'Flash', 'Table', 'HorizontalRule'],
#             ['TextColor', 'BGColor'],
#             ['Smiley', 'SpecialChar'], ['Source'],
#             ['JustifyLeft','JustifyCenter','JustifyRight','JustifyBlock'],
#             ['NumberedList','BulletedList'],
#             ['Indent','Outdent'],
#             ['Maximize'],
#         ],
#         'extraPlugins': ','.join([
#                     'uploadimage', # the upload image feature
#                     # your extra plugins here
#                     'div',
#                     'autolink',
#                     'autoembed',
#                     'embedsemantic',
#                     'autogrow',
#                     'justify',
#                     'liststyle',
#                     'indent',
#                     'image2',
#                     'iframe',
#                     'embed',
#                     # 'devtools',
#                     'widget',
#                     'lineutils',
#                     'clipboard',
#                     'dialog',
#                     'dialogui',
#                     'elementspath',
#                 ]),
#         # 'extraPlugins': 'justify,liststyle,indent,image2,iframe,embed,embedbase,embedsemantic',
#         'embed_provider': '//youtube.com/api/oembed-proxy?resource-url={url}&callback={callback}',
#         'allowedContent': True,
#         'height': 300,
#         'width': 800,
#     },
# }
CKEDITOR_CONFIGS = {
    'default': {
        'skin': 'moono',
        # 'skin': 'office2013',
        'toolbar_Basic': [
            ['Source', '-', 'Bold', 'Italic']
        ],
        'toolbar_YourCustomToolbarConfig': [
            {'name': 'document', 'items': ['Source', '-', 'Save', 'NewPage', 'Preview', 'Print', '-', 'Templates']},
            {'name': 'clipboard', 'items': ['Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord', '-', 'Undo', 'Redo']},
            {'name': 'editing', 'items': ['Find', 'Replace', '-', 'SelectAll']},
            {'name': 'forms',
             'items': ['Form', 'Checkbox', 'Radio', 'TextField', 'Textarea', 'Select', 'Button', 'ImageButton',
                       'HiddenField']},
            '/',
            {'name': 'basicstyles',
             'items': ['Bold', 'Italic', 'Underline', 'Strike', 'Subscript', 'Superscript', '-', 'RemoveFormat']},
            {'name': 'paragraph',
             'items': ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Blockquote', 'CreateDiv', '-',
                       'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock', '-', 'BidiLtr', 'BidiRtl',
                       'Language']},
            {'name': 'links', 'items': ['Link', 'Unlink', 'Anchor']},
            {'name': 'insert',
             'items': ['Image', 'Flash', 'Table', 'HorizontalRule', 'Smiley', 'SpecialChar', 'PageBreak', 'Iframe', 'Embed']},
            '/',
            {'name': 'styles', 'items': ['Styles', 'Format', 'Font', 'FontSize']},
            {'name': 'colors', 'items': ['TextColor', 'BGColor']},
            {'name': 'tools', 'items': ['Maximize', 'ShowBlocks']},
            {'name': 'about', 'items': ['About']},
            '/',  # put this to force next toolbar on new line
            {'name': 'yourcustomtools', 'items': [
                # put the name of your editor.ui.addButton here
                'Preview',
                'Maximize',

            ]},
        ],
        'toolbar': 'YourCustomToolbarConfig',  # put selected toolbar config here
        # 'toolbarGroups': [{ 'name': 'document', 'groups': [ 'mode', 'document', 'doctools' ] }],
        # 'height': 291,
        # 'width': '100%',
        # 'filebrowserWindowHeight': 725,
        # 'filebrowserWindowWidth': 940,
        # 'toolbarCanCollapse': True,
        # 'mathJaxLib': '//cdn.mathjax.org/mathjax/2.2-latest/MathJax.js?config=TeX-AMS_HTML',
        'tabSpaces': 4,
        'extraPlugins': ','.join([
            'uploadimage', # the upload image feature
            # your extra plugins here
            'div',
            'autolink',
            'autoembed',
            'embedsemantic',
            'autogrow',
            'image2',
            'iframe',
            'embed',
            # 'devtools',
            'widget',
            'lineutils',
            'clipboard',
            'dialog',
            'dialogui',
            'elementspath'
        ]),
        'embed_provider': '//www.youtube.com/embed?url={url}&format=json',
        'allowedContent': True,
    }
}