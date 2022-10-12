from pathlib import Path
import environ
# Build paths inside the project like this: BASE_DIR / 'subdir'.

BASE_DIR = Path(__file__).resolve().parent.parent

env=environ.Env(
    DEBUG=(bool, False)
)

environ.Env.read_env(BASE_DIR / ".env")


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY =env("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG =env("DEBUG")

ALLOWED_HOSTS = env.list("DJANGO_ALLOWED_HOST")



# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'main.apps.MainConfig',
    'djcelery_email',
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

ROOT_URLCONF = 'dj_celery_proj.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'dj_celery_proj.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }


DATABASES = {
    'default': {
        'ENGINE': env('SQL_ENGINE'),
        'NAME':env('POSTGRES_DATABASE'),
        'USER':env('POSTGRES_USER'),
        'PASSWORD':env('POSTGRES_PASSWORD'),
        'HOST':env('POSTGRES_HOST'),
        'PORTS':env('POSTGRES_PORT'),
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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'



DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

#email configuration
#EMAIL_BACKEND = 'djcelery_email.backends.CeleryEmailBackend'
EMAIL_BACKEND='django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST ='smtp.mailtrap.io'
EMAIL_HOST_USER ='5e4e0303e552ba'
EMAIL_HOST_PASSWORD ='37bc0278ef91b7'
EMAIL_PORT ='2525'
DEFAULT_FROM_EMAIL='info@henryyoutube.com'
SITE_NAME='django youtube tutorial'
DOMAIN='localhost:8080'


#CELERY CONFIGURATIONS
CELERY_BROKER_URL=env("CELERY_BROKER")
CELERY_RESULT_BACKEND=env("CELERY_BACKEND")
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = "UTC"

