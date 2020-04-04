from django.urls import path
from estimator import views
from estimator.views import HospitalDetailView

urlpatterns = [
    path("", views.home, name="home"),
    path("hospital/", views.create_hospital_page, name="create_hospital"),
    path("all/", views.get_all_hospitals, name="all"),
    path("hospital/<int:pk>/", HospitalDetailView.as_view(),
         name="hospital_detail"),
]
