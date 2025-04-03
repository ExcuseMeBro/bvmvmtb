from pathlib import Path
from django.utils.translation import gettext_lazy as _
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv('DEBUG', 'False') == 'True'

ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS","127.0.0.1").split(",")

# Application definition

INSTALLED_APPS = [
    'django_daisy',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'backend',
    'rest_framework',
    'drf_yasg',  # Swagger uchun
    'corsheaders',
    'modeltranslation',
    'ckeditor',
    'ckeditor_uploader',
]

# CKEditor Configuration
CKEDITOR_UPLOAD_PATH = 'uploads/'
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',
        'height': 300,
        'width': '100%',
    },
}

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mysite.urls'

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

WSGI_APPLICATION = 'mysite.wsgi.application'

APPEND_SLASH = True

# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': os.getenv('DB_HOST'),
        'PORT': os.getenv('DB_PORT'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'uz'

MODELTRANSLATION_DEFAULT_LANGUAGE = 'uz'

MODELTRANSLATION_LANGUAGES = ('uz', 'ru')

MODELTRANSLATION_FALLBACK_LANGUAGES = {
    'default': ('uz', 'ru'),
}

MODELTRANSLATION_LANGUAGES_CHOICES = (
    ('uz', _('Uzbek (Cyrillic)')),
    ('ru', _('Russian')),
)

LANGUAGES = (
    ('uz', _('Uzbek (Cyrillic)')),
    ('ru', _('Russian')),
)

LOCALE_PATHS = [
    BASE_DIR / "locale",
]

TIME_ZONE = 'UTC'

USE_I18N = True
USE_L10N = True

USE_TZ = True
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'

STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

DAISY_SETTINGS = {
    'SITE_TITLE': 'MYSITE',
    'SITE_HEADER': 'MYSITE',
    'INDEX_TITLE': 'Hi, welcome to your dashboard',
    'SITE_LOGO': '/static/admin/img/daisyui-logomark.svg',
    'EXTRA_STYLES': [],
    'EXTRA_SCRIPTS': [],
    'LOAD_FULL_STYLES': False,
    'SHOW_CHANGELIST_FILTER': False,
    'APPS_REORDER': {
        'auth': {
            'icon': 'fa-solid fa-person-military-pointing',
            'name': 'Group',
            'hide': False,
            'app': 'users',
            'divider_title': "Management",
        },
        'social_django': {
            'icon': 'fa-solid fa-users-gear',
        },
        'backend': {
            'icon': 'fa-solid fa-user-group',
            'name': 'Users MNG',
            'hide': False,
            'app': 'clients',
        },
    },
}

# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "https://buxedu.uz"
]

# CORS settings
CORS_ALLOW_ALL_ORIGINS = False

# CSRF settings
CSRF_TRUSTED_ORIGINS = [
    "https://buxedu.uz"
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
}