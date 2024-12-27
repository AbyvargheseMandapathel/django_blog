from django.urls import path
from blog import views
# from .views import home

urlpatterns = [
    path('',views.home,name = 'home'),
    path('login/',views.login,name = 'login'),
    path('signup/',views.signup,name = 'signup'),
]
