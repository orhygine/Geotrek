from .default import *  # NOQA

#
# Django Development
# ..........................

DEBUG = True
TEMPLATE_DEBUG = True

SOUTH_TESTS_MIGRATE = False  # Tested at settings.tests

#
# Developper Toolbar
# ..........................

INSTALLED_APPS = (
    # 'debug_toolbar',
    'django_extensions',
) + INSTALLED_APPS

#
# Use some default tiles
# ..........................

LEAFLET_CONFIG['TILES'] = [
    (gettext_noop('Scan'), 'http://{s}.tile.osm.org/{z}/{x}/{y}.png', '(c) OpenStreetMap Contributors'),
    (gettext_noop('Ortho'), 'http://{s}.tiles.mapbox.com/v3/openstreetmap.map-4wvf9l0l/{z}/{x}/{y}.jpg', '(c) MapBox'),
]
LEAFLET_CONFIG['OVERLAYS'] = [
    (gettext_noop('Coeur de parc'), 'http://{s}.tilestream.makina-corpus.net/v2/coeur-ecrins/{z}/{x}/{y}.png', 'Ecrins'),
]

LEAFLET_CONFIG['SRID'] = 3857

LOGGING['loggers']['geotrek']['level'] = 'DEBUG'
LOGGING['loggers']['']['level'] = 'DEBUG'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
