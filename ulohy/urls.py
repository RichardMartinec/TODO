from django.urls import path
from . import views

urlpatterns = [
    path('', views.zoznam_uloh, name='zoznam_uloh'),
    path('hotovo/<int:id>/', views.oznac_hotovu, name='oznac_hotovu'),
    path('nova/', views.pridat_ulohu, name='pridat_ulohu'),
]