import os


def gettext_noop(s):
    return s


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DEBUG = True

ADMINS = [('Mehdi Bagheri', 'mibiir@gmail.com')]

ALLOWED_HOSTS = []

TIME_ZONE = 'Asia/Tehran'

USE_TZ = True

LANGUAGE_CODE = 'fa-ir'

LANGUAGES = [('fa', gettext_noop('Persian'))]

LOCALE_PATHS = [os.path.join(BASE_DIR, 'locale')]

USE_L10N = True

SERVER_EMAIL = 'notes@notes.com'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'notes_db',
    },
}

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'notes',
]

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

SECRET_KEY = 'ncr%qxd@3jwh$=0**4p7krnw*@$r!=$hi9&ud78pgpdf(m8n_p4'

MEDIA_ROOT = os.path.join(BASE_DIR, 'notes', 'media/')
MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(BASE_DIR, 'notes', 'static/')
STATIC_URL = '/static/'

FILE_UPLOAD_MAX_MEMORY_SIZE = 52428800  # i.e. 50 MB

WSGI_APPLICATION = 'notes.wsgi.application'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

SESSION_EXPIRE_AT_BROWSER_CLOSE = True

AUTH_PASSWORD_VALIDATORS = [
    # {
    #     'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    # },
]

ROOT_URLCONF = 'notes.urls'
