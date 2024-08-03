from .base import *

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)
# os파일에 저장한 시크릿키 불러오기
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))
SECRET_KEY = env("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ["*"]

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "django", #생성한 DB 명
        "USER": "django",
        "PASSWORD": "password1234",
        "HOST": "mariadb",
        "PORT": "3306",
    }
}