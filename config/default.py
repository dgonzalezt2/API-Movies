from decouple import config

SECRET_KEY = config('SECRET_KEY', default='123447a47f563e90fe2db0f56b1b17be62378e31b7cfd3adc776c59ca4c75e2fc512c15f69bb38307d11d5d17a41a7936789')
PROPAGATE_EXCEPTIONS = config('PROPAGATE_EXCEPTIONS', default=True, cast=bool)
# Database configuration
SQLALCHEMY_DATABASE_URI = config('SQLALCHEMY_DATABASE_URI', default='postgres://dgonzalez2:12345@postgres:5432/api-movies')
SQLALCHEMY_TRACK_MODIFICATIONS = config('SQLALCHEMY_TRACK_MODIFICATIONS', default=False, cast=bool)
SHOW_SQLALCHEMY_LOG_MESSAGES = config('SHOW_SQLALCHEMY_LOG_MESSAGES', default=False, cast=bool)
ERROR_404_HELP = config('ERROR_404_HELP', default=False, cast=bool)
