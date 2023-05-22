import os
from .base import *  # noqa

DEBUG = False

ADMINS = [
    ('Adzmart', 'adzmartdotcom@gmail.com'),
    ('Adetola Abiodun', 'tola.adet@gmail.com'),
    ('Oluwafemi Adeniba', 'oadeniba@gmail.com'),
    ('Kehinde Adewusi', 'kehinde.adewusi@gmail.com'),
]
MANAGERS = ADMINS

DEFAULT_FROM_EMAIL = os.getenv('ADZMART_EMAIL_FROM_EMAIL', 'Adzmart <notifications@email.adzmart.com>')
SERVER_EMAIL = os.getenv('ADZMART_EMAIL_FROM_EMAIL', 'notifications@email.adzmart.com')
EMAIL_BACKEND = os.getenv('ADZMART_EMAIL_BACKEND', 'anymail.backends.sendgrid.EmailBackend')
EMAIL_HOST = os.getenv('ADZMART_EMAIL_HOST', 'smtp.sendgrid.net')
EMAIL_PORT = os.getenv('ADZMART_EMAIL_PORT', '587')
EMAIL_HOST_USER = os.getenv('ADZMART_EMAIL_USER', 'apikey')
EMAIL_HOST_PASSWORD = os.getenv('ADZMART_EMAIL_PASSWORD')
EMAIL_USE_TLS = True
ANYMAIL = {
    "SENDGRID_API_KEY": os.getenv('ADZMART_EMAIL_PASSWORD'),
    "SENDGRID_SENDER_DOMAIN": os.getenv('ADZMART_ESP_DOMAIN', 'email.adzmart.com'),
}
