from django.urls import path
from .views import create_station, station_list, station_detail, generate_pdf

urlpatterns = [
    path('', station_list, name='station_list'),
    path('new/', create_station, name='create_station'),
    path('<int:pk>/', station_detail, name='station_detail'),
    path('pdf/<int:pk>/', generate_pdf, name='generate_pdf'),
]
