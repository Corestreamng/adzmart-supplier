import os
import cloudinary
import cloudinary.uploader
import cloudinary.api

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PARENT_DIR = os.path.abspath(os.path.join(BASE_DIR, '..'))

SECRET_KEY = os.environ.get("ADZMART_SECRET_KEY","9qiyn1-*yi%%2b0^nv^l$%=^9eaqf2(j$n_1+jz4)nnifkv3jn")

INSTALLED_APPS = [
    'grappelli',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'widget_tweaks',
    'apps',
    'apps.catalog',
    'apps.authentication',
    'crispy_forms',
    'cloudinary',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'adzmart.core.middleware.RejectAnonymousUsersMiddleware',
]

ROOT_URLCONF = 'adzmart.urls'
AUTH_EXEMPT_ROUTES = ['supplier_register', 'activate',
                      'forgot_password', 'password_reset_confirm', 'login', 'logout']
LOGIN_URL = '/auth/login/'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, "templates"),
        ],
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

CRISPY_TEMPLATE_PACK = 'bootstrap4'

WSGI_APPLICATION = 'adzmart.wsgi.application'

DATABASES = {
    "default": {
        "ENGINE": os.environ.get("ADZMART_DB_ENGINE", "django.db.backends.postgresql"),
        "NAME": os.environ.get("ADZMART_DB_NAME", "adzmart_supplier"),
        "USER": os.environ.get("ADZMART_DB_USER","admin"),
        "PASSWORD": os.environ.get("ADZMART_DB_PASSWORD","18781875"),
        "HOST": os.environ.get("ADZMART_DB_HOST", "127.0.0.1"),
        "PORT": os.environ.get("ADZMART_DB_PORT", "5432"),
        "TEST": {
            "NAME": "adzmart_test",
        },
    }
}

# custom user model
AUTH_USER_MODEL = "authentication.User"

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

TIME_ZONE = 'Africa/Lagos'

USE_I18N = True

USE_L10N = True

USE_TZ = True


STATIC_URL = os.environ.get('ADZMART_STATIC_URL', default='static/')
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(PARENT_DIR, 'static')

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(PARENT_DIR, 'media')

GRAPPELLI_ADMIN_TITLE = "Adzmart"

IMPORT_EXPORT_USE_TRANSACTIONS = True
IMPORT_EXPORT_SKIP_ADMIN_LOG = True

EMAIL_BACKEND = os.environ.get(
    'ADZMART_EMAIL_BACKEND', default='django.core.mail.backends.console.EmailBackend')

ALLOWED_HOSTS = os.environ.get("ADZMART_ALLOWED_HOSTS","http://127.0.0.1:3000,http://localhost:3000").split(",")

CSRF_TRUSTED_ORIGINS = os.getenv("ADZMART_TRUSTED_ORIGINS","http://127.0.0.1:3000,http://localhost:3000").split(',')

# enables django to understand SSL is terminated at the reverse proxy
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Cloudinary config
cloudinary.config( 
  cloud_name = os.environ.get("ADZMART_CLOUDINARY_CLOUD_NAME",'dxeetijm3'), 
  api_key = os.environ.get("ADZMART_CLOUDINARY_API_KEY",'281356359181438'), 
  api_secret = os.environ.get("ADZMART_CLOUDINARY_API_SECRET",'v3Ah3MfSdwBM5rGrxp-FD2wnExo') 
)
