from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('add_cve', views.add_cve, name='add-cve'),
    path('search_cve', views.search_cve, name='search-cve'),
    path('list_cve', views.list_cve, name='list-cve'),
    path('show_cve/<cve_id>', views.show_cve, name='show-cve'),
    path('upload_json', views.upload_json, name='upload_json'),
    path('show_json', views.show_json, name='show_json')
]
