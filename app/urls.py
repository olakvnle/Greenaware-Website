from django.urls import path
from app.views import (IndexView, APIView, DashboardView, ObservationView, ObservationRecordView,
                       SubscriberAPIView, SubscriberDashboardView, SubscriberPriceAPIView, CourseSubmitView,
                       CourseView, UserView, AboutView, PricingView, PricingPlanView,ObserverView,
                       ContactView,SubscriberPriceAPIView,ObserverUserView, ObserverView)

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('about/', AboutView.as_view(), name='about'),
    path('api/', APIView.as_view(), name='api'),
    path('pricing/', PricingView.as_view(), name='pricing'),
    path('pricing_plan/', PricingPlanView.as_view(), name='pricing_plan'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('observer/', ObserverView.as_view(), name='observer'),
    path('observer/dashboard/', DashboardView.as_view(), name='dashboard'),
    path('observation/create/', ObservationView.as_view(), name='observation'),
    path('observation/view/', ObservationRecordView.as_view(), name='observation_data'),
    path('subscriber/dashboard/', SubscriberDashboardView.as_view(), name='subscriber_dashboard'),
    path('subscriber/api_access/', SubscriberAPIView.as_view(), name='api_access'),
    path('subscriber/pricing/', SubscriberPriceAPIView.as_view(), name='api_pricing'),
    path('submit-course/', CourseSubmitView.as_view(), name='submit-course'),
    path('courses/', CourseView.as_view(), name='courses'),
    path('users/profiles/', UserView.as_view(), name='users'),
    path('user/profiles/', ObserverUserView.as_view(), name='user'),
    path('observer/register/', ObserverView.as_view(), name='observer'),

]
