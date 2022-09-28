from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('QueryService.urls'))
]

admin.site.site_header = "SCVM Admin"
admin.site.site_title = "Administration"
admin.site.index_title = "SCVM Administration Page"