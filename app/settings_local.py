# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'b0e@^m&tccz11$w59qov$lhn-97!(%wfn-gray-c*x)^a$wx=2'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'articles_django',
        'USER': 'postgres',
        'PASSWORD': '12345',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

