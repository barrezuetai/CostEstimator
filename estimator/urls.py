from django.urls import path
from estimator import views

urlpatterns = [
    path("", views.home, name="home"),
]