
from django.urls import path

from app.views import (IndexView, ObserverRegisterView, APIView, LoginView,DashboardView,ObservationView,CourseView,UserView)

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('observer/', ObserverRegisterView.as_view(), name='observer'),
    path('get-api/', APIView.as_view(), name='get-api'),
    path('observer/login/', LoginView.as_view(), name='login'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('observation/', ObservationView.as_view(), name='observation'),
    path('courses/', CourseView.as_view(), name='courses'),
    path('users/profiles/', UserView.as_view(), name='users')
]