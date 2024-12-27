from django.urls import path
from blog import views
# from .views import home

urlpatterns = [
    path('',views.home,name = 'home'),
    path('login',views.user_login,name = 'login'),
    path('signup',views.user_signup,name = 'signup'),
    path('dashboard',views.dashboard,name = 'dashboard'),
]
