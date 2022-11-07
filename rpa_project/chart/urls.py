from django.urls import path

from . import views

app_name = 'chart'

urlpatterns = [
    path('', views.index, name='index'),
    path('nation/', views.nation, name='nation'),
    path('sea/', views.sea, name='sea'),
]
