# Contact-me-app
a reusable, plug-able api based django app. with django rest framework
## options:
* pluggable in other apps
* send verification email
* set is readed status by admin
* send mass email to all which contact me
* filter by date for admin

## Installation
### Linux
1. git clone https://github.com/F4R4N/movie-quote.git
2. apt install python3
3. cd movie-quote
4. ` python3 -m venv venv`
5. source venv/bin/activate
6. python3 manage.py migrate
7. python3 manage.py runserver
8. open browser in 127.0.0.1:8000

### Windows
1. git clone https://github.com/F4R4N/movie-quote.git or download directly
2. install [python3](https://www.python.org/downloads/)
3. cd movie-quote
4. `python -m venv venv`
5. venv\Scripts\activate
6. python manage.py migrate
7. python manage.py runserver
8. open browser in 127.0.0.1:8000


## settings
app should configure for the project that import in.

### Default Settings
``` python
DEFAULT_CONTACT_US_SETTINGS = {
  "APP_NAME": None,
  "SEND_MAIL": False,
  "MAIL_SUBJECT": " Contact Us ",
  "MESSAGE": "\nwe got your email. we will respond as soon as possible.\n\nBest Regards, ",
}
```
and should include email backend settings in project ssettings.py if SEND_MAIL=True
``` python
EMAIL_USE_TLS = True
EMAIL_HOST = SMTP
EMAIL_PORT = 587
EMAIL_HOST_USER = EMAIL
EMAIL_HOST_PASSWORD = PASSWORD
```
