from django.urls import path
from . import views

app_name = 'disease_app'

urlpatterns = [
    path('', views.home_view, name='home'),
    path('result/<int:image_id>/', views.result_view, name='result'),
]
