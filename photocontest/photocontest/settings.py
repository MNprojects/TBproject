import os


BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'byv$u8%mn)ypjdo$_zo=bcl3wdg=qd_4iapm6q5c5#58%wrjok'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


INSTALLED_APPS = [
    'submissions.apps.SubmissionsConfig',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'social_django',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'social_django.middleware.SocialAuthExceptionMiddleware',
]

ROOT_URLCONF = 'photocontest.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['./templates',],
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

WSGI_APPLICATION = 'photocontest.wsgi.application'




""" ------------------------------------------------------------------------------------------------------
    My Code - Had to edit the database details as Django ships with sqlite3. To be changed so datebase is local to repository without plain text login details.
------------------------------------------------------------------------------------------------------ """

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'photos',
        'USER': 'root',
        # Bad practice, only for testing purposes
        'PASSWORD': 'SQL8i,lL1wJ',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
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
# Changed time zone
TIME_ZONE = 'Europe/London'

USE_I18N = True

USE_L10N = True

USE_TZ = True
	

STATIC_URL = '/static/'

LOGIN_REDIRECT_URL = '/'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)

MEDIA_ROOT = os.path.join(BASE_DIR, 'img')
MEDIA_URL = '/'

AUTHENTICATION_BACKENDS = (
    'social_core.backends.facebook.FacebookOAuth2',

    'django.contrib.auth.backends.ModelBackend',
)

SOCIAL_AUTH_FACEBOOK_KEY = '1768355136568203'  # App ID
SOCIAL_AUTH_FACEBOOK_SECRET = '3bce17d90205b8c67cc5a22e8dd58432'

LOGIN_URL = 'photocontest_login'
LOGOUT_URL = 'photocontest_logout'
