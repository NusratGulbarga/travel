from django.urls import path
from . import views

urlpatterns = [
    path('', views.destination_list, name='destination_list'),
    path('tour-package/<int:package_id>/', views.tour_package_detail, name='tour_package_detail'),
    path('book/<int:package_id>/', views.book_tour, name='book_tour'),
]
