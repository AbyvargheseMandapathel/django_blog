from django.urls import path
from blog import views
# from .views import home

urlpatterns = [
    path('',views.home,name = 'home'),
]
