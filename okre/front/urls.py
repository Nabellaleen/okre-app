from django.urls import path
from . import views

app_name = 'front'

urlpatterns = [
    path('', views.navigation_view, name='navigation'),
]
