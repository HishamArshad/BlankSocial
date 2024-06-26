"""
Django settings for backend project.

Generated by 'django-admin startproject' using Django 4.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import dj_database_url
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
from dotenv import load_dotenv
import os

load_dotenv()


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []
 
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
 
 
EMAIL_FROM = os.environ.get('EMAIL_FROM')
EMAIL_BCC = ''  # Leave this empty if you don't need BCC
EMAIL_HOST = os.environ.get('EMAIL_HOST')

EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')  # Replace 'your_gmail_password' with your Gmail password
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False
EMAIL_PORT = 587
# Application definition


 
 
 

INSTALLED_APPS = [
    'daphne',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
	'rest_framework.authtoken',
    # 'oauth2_provider',
    'social_django',
    'corsheaders',

    # 'rest_framework_social_oauth2',
    'authemail',
    'accounts',
    'chat',
    'channels'
]
ASGI_APPLICATION = "backend.asgi.application"
CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [("127.0.0.1", 6379)],
        },
    },
}
STREAM_API_KEY = os.environ.get('STREAM_API_KEY') # https://getstream.io/dashboard/
STREAM_API_SECRET = os.environ.get('STREAM_API_SECRET')
 
AUTH_USER_MODEL = 'accounts.myUser'
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
     
    ),
}
 
 
LOGIN_URL = 'login'  # Set this to the URL where users are redirected if they need to log in
LOGIN_REDIRECT_URL = '/'  # Set this to the desired URL where users are redirected after a successful login
AUTH_EMAIL_VERIFICATION = True

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'backend.urls'

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
         
                # 'social_django.context_processors.backends',
                # 'social_django.context_processors.login_redirect',
            ],
        },
    },
]
# Make sure 'APP_DIRS' is set to True
TEMPLATES[0]['APP_DIRS'] = True

# Specify the path to your app-specific templates directory
TEMPLATES[0]['DIRS'].append(os.path.join(BASE_DIR, 'accounts/templates'))

WSGI_APPLICATION = 'backend.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
       'default': dj_database_url.config(
        # Replace this value with your local database's connection string.
        default='postgres://mysite_n7e9_user:o5RnV0YH5G0PZWfisOWDGooZjVSKFaTA@dpg-cpbg1g5ds78s73eunkug-a.oregon-postgres.render.com/mysite_n7e9',
        conn_max_age=600
    )
    # 'default': {
    #     "ENGINE": "django.db.backends.mysql",
    #     "NAME": "social",
   
    #     "HOST": "localhost",
    #     "PASSWORD": "kkllBB#46",
    #     "USER": "root",
    #     "PORT": 3306,
    # },
    
}

 
# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field
if not DEBUG:
    # Tell Django to copy static assets into a path called `staticfiles` (this is specific to Render)
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
    # Enable the WhiteNoise storage backend, which compresses static files to reduce disk use
    # and renames the files with unique names for each version to support long-term caching
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
# CORS settings
CORS_ALLOW_ALL_ORIGINS = False  # Set to True to allow all origins (not recommended for production)
CORS_ALLOW_CREDENTIALS = True   # Set to True if your frontend sends cookies with requests
CORS_ALLOWED_ORIGINS = [        # List the allowed origins (e.g., your frontend domain)
    "http://localhost:5173",    # Add the actual domain of your React app
]
 
