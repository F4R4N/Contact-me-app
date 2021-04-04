# Contact-me-app
a reusable, plug-able api based django app. with django rest framework
## options:
* pluggable in other apps
* send verification email
* set is readed status by admin
* send mass email to all which contact me
* filter by date for admin
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
