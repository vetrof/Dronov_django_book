from django.urls import path
from bboard.views import index_view

urlpatterns = [
    path('', index_view),
]

