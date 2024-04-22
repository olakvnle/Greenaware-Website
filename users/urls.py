from django.urls import path
from .views import ActivateObserverView
from users.views import ( LogoutView,LoginView,ObserverRegisterationView,SubscriberRegisterationView)

urlpatterns = [
    path('observer/', ObserverRegisterationView.as_view(), name='observer'),
    path('register-subscriber/', SubscriberRegisterationView.as_view(), name='register-subscriber'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('activate/<uidb64>/<token>', ActivateObserverView.as_view(), name='activate'),
]