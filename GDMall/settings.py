"""
Django settings for GDMall project.

Generated by 'django-admin startproject' using Django 2.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'h1#ym_$=yi!2*dhsae+m2p$ws_73!2xs)0=7@j6dvk(_e0vz50'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'xadmin',  # xadmin后台管理
    'crispy_forms',  # xadmin后台管理
    'apps.user',  # 用户模块
    'apps.goods',  # 商品模块
    'apps.cart',  # 购物车模块
    'apps.pay',  # 支付模块
    'apps.order', # 订单模块
    # 'werkzeug_debugger_runserver',    # https
    # 'django_extensions',  # https
    'rest_framework',  # 添加rest_framework
]

# 配置使用到的用户模型类
AUTH_USER_MODEL = 'user.User'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'GDMall.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'common.processor.ali_media',  # aliyun
            ],
        },
    },
]

WSGI_APPLICATION = 'GDMall.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'gdmall',
        'USER': 'root',
        'PASSWORD': '123456',
        'HOST': '127.0.0.1'
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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

# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

# 静态文件配置
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
# 指定收集静态文件的路径
STATIC_ROOT = '/opt/static/GDMall'

# 证书配置
# SESSION_COOKIE_SECURE=True
# SESSION_COOKIE_HTTPONLY=True
# SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTOCOL', 'https')

# 阿里云oss
ACCESS_KEY_ID = "LTAI5cuJmRKFt1fW"
ACCESS_KEY_SECRET = "Km5xbIeCN7ockiONQiX6hY0FQFIOzh"
END_POINT = "oss-cn-shenzhen.aliyuncs.com"
PREFIX_URL = 'http://'
BUCKET_NAME = "grotesquery"
ALIYUN_OSS_CNAME = ""  # 自定义域名，如果不需要可以不填写
BUCKET_ACL_TYPE = "public-read"  # private, public-read, public-read-write
DEFAULT_FILE_STORAGE = 'aliyun_oss2_storage.backends.AliyunMediaStorage'
MEDIA_URL = '/media/'
MEDIA_ROOT = "media"
ALI_MEDIA_URL = PREFIX_URL + BUCKET_NAME + "." + END_POINT + '/media/'

# redis配置
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://:123456@127.0.0.1:6379/0",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    },
    "UserToken": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://:123456@127.0.0.1:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    },
    "Cart": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://:123456@127.0.0.1:6379/2",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}
# Django 默认可以使用任何 cache backend 作为 session backend, 将 django-redis 作为 session 储存后端不用安装任何额外的 backend
SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = "default"
