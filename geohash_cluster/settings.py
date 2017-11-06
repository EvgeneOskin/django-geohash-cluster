from django.conf import settings as django_settings


class Settings(object):

    default_geohash_length = 25

    def __init__(self):
        self.GEOHASH_LENGTH = getattr(
            django_settings, 'GEOHASH_LENGTH', self.default_geohash_length
        )


settings = Settings()
