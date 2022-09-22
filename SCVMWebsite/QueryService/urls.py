from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('add_cve', views.add_cve, name='add-cve'),
    path('search_cve', views.search_cve, name='search-cve')
]
