from .base import *

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)
# os파일에 저장한 시크릿키 불러오기
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))
SECRET_KEY = env("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
ALLOWED_HOSTS = ["*"]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}