from django.urls import path
from estimator import views

urlpatterns = [
    path("", views.home, name="home"),
    path("hospital/<int:pk>/", HospitalDetailView.as_view(),
         name="hospital_detail"),
]
