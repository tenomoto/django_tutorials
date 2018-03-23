from django.urls import path

from . import views

urlpatterns = [
    path('memberonly/', views.memberonly, name='memberonly'),
    path('', views.index, name='index'),
]