
from django.contrib import admin
from django.urls import path, include

from bboard.views import index_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bboard/', include('bboard.urls')),
]
