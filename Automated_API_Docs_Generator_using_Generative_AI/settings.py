from pathlib import Path
import os
from dotenv import load_dotenv

# ---------------- BASE DIR ---------------- #
BASE_DIR = Path(__file__).resolve().parent.parent

# ---------------- SECURITY ---------------- #
load_dotenv()

SECRET_KEY = os.getenv('SECRET_KEY', 'django-insecure-temp-key')

DEBUG = False

ALLOWED_HOSTS = ['*']  # for Render

# ---------------- APPS ---------------- #
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'users',
    'admins',
]

# ---------------- MIDDLEWARE ---------------- #
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',

    # ✅ ADD THIS (important for static files in production)
    'whitenoise.middleware.WhiteNoiseMiddleware',

    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# ---------------- URL CONFIG ---------------- #
ROOT_URLCONF = 'Automated_API_Docs_Generator_using_Generative_AI.urls'

# ---------------- TEMPLATES ---------------- #
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# ---------------- WSGI ---------------- #
WSGI_APPLICATION = 'Automated_API_Docs_Generator_using_Generative_AI.wsgi.application'

# ---------------- DATABASE ---------------- #
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# ---------------- PASSWORD VALIDATION ---------------- #
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# ---------------- INTERNATIONAL ---------------- #
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# ---------------- STATIC FILES ---------------- #
STATIC_URL = '/static/'

STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# ✅ WhiteNoise config
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# ---------------- MEDIA FILES ---------------- #
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# ---------------- ENV VARIABLES ---------------- #
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# ---------------- DEFAULT FIELD ---------------- #
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'