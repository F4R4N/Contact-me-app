
DEFAULT_CONTACT_US_SETTINGS = {
	'APP_NAME': None,
	'SEND_MAIL': False,
	'MAIL_SUBJECT': " Contact Us ",
	'MESSAGE': "dear '%s',\n we got your email. we will response as soon as possible.\n\nBest Regards '%s'"
}

try:
	from django.conf.settings import CONTACT_US_SETTINGS
except ImportError:
	print("ERROR: No CONTACT_US_SETTINGS Found At Projects settings.py")

fields = ["APP_NAME", "SEND_MAIL", "MAIL_SUBJECT", "MESSAGE"]

for field in fields:
	if field in CONTACT_US_SETTINGS:
		DEFAULT_CONTACT_US_SETTINGS[field] = CONTACT_US_SETTINGS[field]

try:
	from django.conf.settings import EMAIL_USE_TLS, EMAIL_HOST, EMAIL_PORT, EMAIL_HOST_USER, EMAIL_HOST_PASSWORD
except ImportError:
	print("ERROR: No Email Configuration Found in projects settings.py." + 'configure : "EMAIL_USE_TLS", "EMAIL_HOST", "EMAIL_PORT", "EMAIL_HOST_USER", "EMAIL_HOST_PASSWORD"' + "or Set SEND_MAIL=False")
