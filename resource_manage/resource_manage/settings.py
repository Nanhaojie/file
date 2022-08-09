"""
Django settings for resource_manage project.

Generated by 'django-admin startproject' using Django 3.2.15.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import os
import configparser
import time
import datetime
import sys

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, os.path.join(BASE_DIR, "apps"))

config = configparser.ConfigParser()
config.read(os.path.join(BASE_DIR, 'conf/dev.conf'))

# DB mysql config
DB_HOST = config.get('db', 'host')
DB_PORT = config.getint('db', 'port')
DB_USER = config.get('db', 'user')
DB_PASSWORD = config.get('db', 'password')
DB_DATABASE = config.get('db', 'database')

# DB redis config
REDIS_HOST = config.get('redis', 'host')
REDIS_PORT = config.getint('redis', 'port')
REDIS_PASSWORD = config.get('redis', 'password')


LOG_FOLDER_PATH = config.get('log', 'log_file_path')
if not LOG_FOLDER_PATH.startswith('/'):
    LOG_FOLDER_PATH = os.path.join(BASE_DIR, LOG_FOLDER_PATH)

if not os.path.exists(LOG_FOLDER_PATH):
    os.makedirs(LOG_FOLDER_PATH)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-28+us96c&2$9yvzbut3#3gkj#0ad8$bhmj%croj35c2&0-7v*^'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*", ]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'drf_yasg',
    'django_filters',
    'file',
    'user',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',  # cors解决跨域问题
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'resource_manage.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'resource_manage.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': DB_HOST,  # 数据库主机
        'PORT': DB_PORT,  # 数据库端口
        'USER': DB_USER,  # 数据库用户名
        'PASSWORD': DB_PASSWORD,  # 数据库用户密码
        'NAME': DB_DATABASE,  # 数据库名字
        'default-character-set': 'utf8',
        'OPTIONS': {'charset': 'utf8mb4'},
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'zh-Hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

REDIS_URL = f'redis://:{REDIS_PASSWORD}@{REDIS_HOST}:{REDIS_PORT}'

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": f'{REDIS_URL}/8',
        "OPTIONS": {
            "PASSWORD": REDIS_PASSWORD,
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    },

    "login_user": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": f'{REDIS_URL}/9',
        "OPTIONS": {
            "PASSWORD": REDIS_PASSWORD,
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,  # 是否禁用已经存在的日志器
    'formatters': {  # 日志信息显示的格式
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(lineno)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(module)s %(lineno)d %(message)s'
        },
        # 详细的日志格式
        'standard': {
            'format': '%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'
        }
    },
    'filters': {  # 对日志进行过滤 todo
        'require_debug_true': {  # django在debug模式下才输出日志
            '()': 'django.utils.log.RequireDebugTrue',
        }
    },
    'handlers': {  # 日志处理方法
        # 默认记录所有日志
        'default': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOG_FOLDER_PATH, 'all-{}.log'.format(time.strftime('%Y-%m-%d'))),
            'maxBytes': 1024 * 1024 * 500,  # 文件大小  500M
            'backupCount': 5,  # 备份数
            'formatter': 'standard',  # 输出格式
            'encoding': 'utf-8',  # 设置默认编码，否则打印出来汉字乱码
        },
        'console': {  # 向终端中输出日志
            'level': 'INFO',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'standard'
        },
    },
    'loggers': {  # 日志器
        'django': {  # 定义了一个名为django的日志器
            'handlers': ['console', 'default'],  # 可以同时向终端与文件中输出日志
            'propagate': True,  # 是否继续传递日志信息
            'level': 'INFO',  # 日志器接收的最低日志级别
        },
    }
}

REST_FRAMEWORK = {
    # 指定DRF框架异常处理的函数
    'EXCEPTION_HANDLER': 'utils.exceptions.exception_handler',
    # 认证设置
    'DEFAULT_AUTHENTICATION_CLASSES': (
        # 引入JWT认证机制，之后客户端请求服务器时，如果传递jwt token
        # 此认证机制会自动校验jwt token的有效性，如果无效直接返回401(未认证)
        # 'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'utils.token_auth.SlideTokenAuthentication',

        # 自定义重写jwt认证方法
        # 'utils.common.CsrfExemptSessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ),
    # 修改默认返回JSON的renderer的类
    'DEFAULT_RENDERER_CLASSES': (
        'utils.render_response.CustomJsonRenderer',
    ),
    # 全局分页设置
    'DEFAULT_PAGINATION_CLASS': 'utils.pagination.StandardResultPagination',
    # 查询过滤功能
    'DEFAULT_FILTER_BACKENDS': ('django_filters.rest_framework.DjangoFilterBackend',)
}

# 认证时间
JWT_AUTH = {
    'JWT_EXPIRATION_DELTA': datetime.timedelta(minutes=30),  # 过期时间 8 小时
    'JWT_RESPONSE_PAYLOAD_HANDLER': 'user.utils.jwt_response_payload_handler',  # 重新定义了返回值的内容；默认只返回token
}

# 我们自定义的用户模型类还不能直接被Django的认证系统所识别，需要在配置文件中告知Django认证系统使用我们自定义的模型类。
AUTH_USER_MODEL = 'user.AccountModel'

# CORS白名单设置
CORS_ORIGIN_WHITELIST = ()
CORS_ALLOW_CREDENTIALS = True  # 允许携带cookie
CORS_ORIGIN_ALLOW_ALL = True

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# 序列化时间格式
SERIALIZER_DATE_TIME_FIELD_FORMAT = "%Y-%m-%d %H:%M:%S"
SERIALIZER_DATE_TIME_FIELD_FORMAT3 = "%Y-%m-%d %H:%M"
SERIALIZER_DATE_TIME_FIELD_FORMAT2 = "%Y年%m月%d日%H时%M分"
SERIALIZER_DATE_FIELD_FORMAT = "%Y-%m-%d"
SERIALIZER_TIME_FIELD_FORMAT = "%H:%M"
FILE_NAME_DATE_TIME_FORMAT = "%Y%m%d%H%M%S%f"

PC_EXP_SECOND = 8 * 60 * 60 + 30 * 60  # 8个半小时
# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

# 文件路径
FILE_PATH = '/home/nhj/upload_files/'

# 文件服务器地址
FS_SERVER = 'http://0.0.0.0:8090/fs/v1/file/'
