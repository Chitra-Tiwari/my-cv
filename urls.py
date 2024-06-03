from . import views
from django.urls import path


urlpatterns=[
    path('',views.welcome),
    path('home',views.home),
    path('form',views.form)
]