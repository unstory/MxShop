"""
Django settings for MxShop project.

Generated by 'django-admin startproject' using Django 3.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import sys
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

sys.path.insert(0, str(BASE_DIR))
sys.path.insert(0, str(BASE_DIR/'apps'))
sys.path.insert(0, str(BASE_DIR/'extra_apps'))
private_key_path = os.path.join(str(BASE_DIR), 'apps/trade/keys/private_2048.txt')
ali_pub_key_path = os.path.join(str(BASE_DIR), 'apps/trade/keys/alipay_key_2048.txt')


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '(6te(=u^u4=v_x=2ylfbg^p_otq83)n1*nyx9e!c3vt5=ol67f'

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
    'DjangoUeditor',
    'xadmin',
    'rest_framework',
    'crispy_forms',
    'users.apps.UsersConfig',
    'goods',
    'trade',
    'user_operation.apps.UserOperationConfig',
    'django_filters',
    'coreschema',
    'rest_framework.authtoken',
    'social_django',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

from corsheaders.defaults import default_headers
CORS_ALLOW_HEADERS = default_headers + (
    'contenttype',
    'content-type',
    'is_authenticated',
    'Authorization',
)
CORS_ALLOW_METHODS = [
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
]
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True

ROOT_URLCONF = 'MxShop.urls'
AUTH_USER_MODEL = 'users.UserProfile'

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
                 'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'MxShop.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'test',        #数据库名字
        'USER': 'root',          #账号
        'PASSWORD': '123456',    #密码
        'HOST': '127.0.0.1',     #IP
        'PORT': '3306',          #端口
        #这里引擎用innodb（默认myisam）
        #因为后面第三方登录时，要求引擎为INNODB
        # 'OPTIONS':{'init_command': 'SET storage_engine=INNODB'}, #这样设置会报错，改为
        "OPTIONS":{"init_command":"SET default_storage_engine=INNODB;"}
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        #'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
    ),
    "DEFAULT_SCHEMA_CLASS": "rest_framework.schemas.AutoSchema",
    #限速设置
    'DEFAULT_THROTTLE_CLASSES': (
            'rest_framework.throttling.AnonRateThrottle',   #未登陆用户
            'rest_framework.throttling.UserRateThrottle'    #登陆用户
        ),
    'DEFAULT_THROTTLE_RATES': {
        'anon': '100/minute',         #每分钟可以请求两次
        'user': '1000/minute'          #每分钟可以请求五次
    },
}

import datetime 
JWT_AUTH = {
    'JWT_EXPIRATION_DELTA': datetime.timedelta(days=1),
    # token前缀
    'JWT_AUTH_HEADER_PREFIX': 'Bearer',
}

#缓存配置
REST_FRAMEWORK_EXTENSIONS = {
    'DEFAULT_CACHE_RESPONSE_TIMEOUT': 5   #5s过期，时间自己可以随便设定
}


CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}

AUTHENTICATION_BACKENDS = (
    'users.views.CustomBackend',
    'social_core.backends.weibo.WeiboOAuth2',
    'social_core.backends.qq.QQOAuth2',
    'social_core.backends.weixin.WeixinOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)

REGEX_MOBILE = "^1[358]\d{9}$|^147\d{8}$|^176\d{8}$"
APIKEY = "xxxxbb8122bc6f8f484ae41eb5xxxxxx"

# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
MEDIA_ROOT = str(BASE_DIR/"media")

import os
MEDIA_URL="/media/"
MEDIA_ROOT=os.path.join(BASE_DIR,"media")

SOCIAL_AUTH_WEIBO_KEY = 'x47092358x'
SOCIAL_AUTH_WEIBO_SECRET = 'x3aae945fb632f5ad775b56daa3d204x'
SOCIAL_AUTH_LOGIN_REDIRECT_URL = 'http://127.0.0.1:8000'
