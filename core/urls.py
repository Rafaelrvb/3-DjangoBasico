from django.urls import path
from core.views import *  # import view functions


urlpatterns = [
    path('', index, name="index"),
    path('contact', contact, name="contact"),
    path('produto/<int:params>', produto, name="produto")
]
