from django.urls import path

from . import views

urlpatterns = [
    path('omlet/', views.omlet),
    path('pasta/', views.pasta),
    path('buter/', views.buter)
]