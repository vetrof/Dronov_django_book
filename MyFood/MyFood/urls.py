"""
URL configuration for temp3 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from foodlist.views import index_page, index_page_type
from question.views import QuestionFormView, CrispyCreateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_page, name='index'),
    path('<int:type_id>/', index_page_type, name='by_type'),
    path('question/', QuestionFormView.as_view(), name='question'),
    path('crispy/', CrispyCreateView.as_view(), name='crispy'),
]
