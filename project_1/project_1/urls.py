
from django.contrib import admin
from django.urls import path, include

from bboard.views import index_view, index_rubric_view

# index/admin/
urlpatterns = [
    path('admin/', admin.site.urls),
]

# index/bboard/
urlpatterns += [
    path('bboard/', index_view, name='board'),
    path('bboard/<int:by_rubric>', index_rubric_view, name='rubrics'),

]