from django.urls import path
from . import views

app_name = 'front'

urlpatterns = [
    path('', views.navigation_view, name='navigation'),
    path('objective/<int:objective_id>', views.objective_view, name='objective'),
]
