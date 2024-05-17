from django.urls import path
# from .views import ActivateObserverView,ActivateUserView
from users.views import ( LogoutView,LoginView,ObserverRegisterationView,
                          ActivateObserverView,ActivateUserView,store_tokens)

urlpatterns = [
    path('register/', ObserverRegisterationView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('activation/<uidb64>/<token>', ActivateUserView.as_view(), name='activation'),
    path('activate-email/<str:uid>/<str:token>/', ActivateObserverView.as_view(), name='activate'),
    path('store-tokens/', store_tokens, name='store_tokens'),

]