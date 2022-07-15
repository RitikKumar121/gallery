from django.urls import path
from . import views

urlpatterns = [
    path('',views.gallery,name='gallery'),
    path('photo/<str:pk>/', views.viewphotos, name='photo'),
    #delete function
    path('delete-product/<str:pk>/', views.deleteproduct, name='delete-prod'),

#    path('photo/', views.viewphotos, name='photo'),
    path('add/', views.addphotos, name='add'),
    path('about/', views.about, name='about'),
]
