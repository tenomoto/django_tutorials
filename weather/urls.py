from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:loc>', views.detail, name='detail'),
]