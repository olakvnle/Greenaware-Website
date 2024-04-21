from django.urls import path
from .views import ActivateObserverView

urlpatterns = [
    # Other URL patterns...
    path('activate/<str:uid>/<str:token>/', ActivateObserverView.as_view(), name='activate'),
]