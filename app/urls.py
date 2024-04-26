
from django.urls import path

from app.views import (IndexView, APIView,DashboardView,ObservationView,CourseView,UserView, AboutView, PricingView, PricingPlanView, ContactView, SubscriberDashboardView, SubscriberAPIView)

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('about/', AboutView.as_view(), name='about'),
    path('api/', APIView.as_view(), name='api'),
    path('pricing/', PricingView.as_view(), name='pricing'),
    path('pricing_plan/', PricingPlanView.as_view(), name='pricing_plan'),
    path('contact/', ContactView.as_view(), name='contact'),
    # path('get-api/', APIView.as_view(), name='get-api'),
    path('observer/dashboard/', DashboardView.as_view(), name='dashboard'),
    path('observation/', ObservationView.as_view(), name='observation'),
    path('courses/', CourseView.as_view(), name='courses'),
    path('users/profiles/', UserView.as_view(), name='users'),
    path('subscriber/dashboard/', SubscriberDashboardView.as_view(), name='dashboard'),
    path('subscriber/api_access/', SubscriberAPIView.as_view(), name='api_access')
] 
