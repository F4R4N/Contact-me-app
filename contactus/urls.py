from django.urls import path
from .views import CreateForm, AdminContactReader

app_name = "contact"

urlpatterns = [
	path("contact/", CreateForm.as_view()),
	path("admin/contact/", AdminContactReader.as_view()),
]