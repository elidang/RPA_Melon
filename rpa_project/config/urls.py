
from django.contrib import admin
from django.urls import path, include
from chart import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('chart/', include('chart.urls')),
]
