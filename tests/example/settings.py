DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}

SITE_ID = 1

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'subdomains.middleware.SubdomainURLRoutingMiddleware',
)

ROOT_URLCONF = 'example.urls.application'
SUBDOMAIN_URLCONFS = {
    None: 'example.urls.marketing',
    'api': 'example.urls.api',
    'www': 'example.urls.marketing',
}

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'example.wsgi.application'

INSTALLED_APPS = (
    'django.contrib.sites',
    'example',
    'subdomains',
)
