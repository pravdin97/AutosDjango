from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('offers', views.offers, name='offers'),
    path('edit', views.edit, name='edit'),
    path('oneitem', views.oneitem, name='oneitem'),
]