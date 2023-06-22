from django.contrib import admin
from django.urls import path
from speaker import views


urlpatterns = [
    path('',views.home),
    path('update/',views.update),
    path('delete/',views.delete),
    path('select/',views.select),

    
]