
from django.urls import path

from app.views import (IndexView, APIView,DashboardView,ObservationView,ObservationRecordView,
                       CourseView,UserView, AboutView, PricingView, PricingPlanView, ContactView)

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('about/', AboutView.as_view(), name='about'),
    path('api/', APIView.as_view(), name='api'),
    path('pricing/', PricingView.as_view(), name='pricing'),
    path('pricing_plan/', PricingPlanView.as_view(), name='pricing_plan'),
    path('contact/', ContactView.as_view(), name='contact'),
    # path('get-api/', APIView.as_view(), name='get-api'),
    path('observer/dashboard/', DashboardView.as_view(), name='dashboard'),
    path('observation/create/', ObservationView.as_view(), name='observation'),
    path('observation/view/', ObservationRecordView.as_view(), name='observation_data'),
    path('courses/', CourseView.as_view(), name='courses'),
    path('users/profiles/', UserView.as_view(), name='users')
] 