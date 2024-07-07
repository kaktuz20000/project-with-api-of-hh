from django.contrib import admin
from django.urls import path
from hh_parser import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('parse/', views.parse, name='parse'),
    path('analytics/', views.analytics, name='analytics'),
]