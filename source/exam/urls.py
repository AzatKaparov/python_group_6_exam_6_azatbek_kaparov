from django.contrib import admin
from django.urls import path
from webapp.views import index_view, create_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_view, name='index'),
    path('note/add/', create_view, name='create'),
]
