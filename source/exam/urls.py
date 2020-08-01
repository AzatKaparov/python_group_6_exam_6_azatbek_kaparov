from django.contrib import admin
from django.urls import path
from webapp.views import index_view, create_view, update_view, delete_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_view, name='index'),
    path('note/add/', create_view, name='create'),
    path('note/<int:pk>/update', update_view, name='update'),
    path('note/<int:pk>/delete', delete_view, name='delete')
]
