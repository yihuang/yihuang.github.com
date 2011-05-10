import os
ROOT = os.path.dirname(os.path.realpath(__file__))
join = os.path.join

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('huangyi', 'yi.codeplayer@gmail.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'sqlite.db',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

TIME_ZONE = 'Asia/Hong_Kong'
LANGUAGE_CODE = 'zh-CN'
SITE_ID = 1

USE_I18N = True
USE_L10N = True

MEDIA_ROOT = join(ROOT, 'media')
MEDIA_URL = '/media/'
STATIC_URL = 't.static.com'
ADMIN_MEDIA_PREFIX = STATIC_URL

SECRET_KEY = '2+x@59@12!1rkq#e6ej)za^*2=uw(_+k=2)3-*vitb%d$+_(0s'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.contrib.messages.context_processors.messages",
)

ROOT_URLCONF = 'codingproj.urls'

TEMPLATE_DIRS = (
    join(ROOT, "templates"),
)

STATICFILES_DIRS = (
    join(ROOT, "static"),
)

SNS = {
    'douban': {
        'app_key': '021e921e86db109c065bb65b949131d4',
        'app_secret': '6be5d7dce18883b8',
    },
    'sina': {
        'app_key': '',
        'app_secret': '',
    },
    'qq': {
        'app_key': '',
        'app_secret': '',
    },
}

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.admin',
    'django.contrib.staticfiles',
    'tagging',
    'snippet',
    'snsauth',
    'codecomment',
)

FORCE_LOWERCASE_TAGS = True
