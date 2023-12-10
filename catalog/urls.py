from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

from catalog import views

urlpatterns = [
        path("menu/", views.index),
]

