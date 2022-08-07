from django.urls import path
from .views import HomeView, SuccesView

urlpatterns = [
    path("", HomeView, name = "home"),
    path("succes/", SuccesView, name="succes")
]