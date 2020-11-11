from django.urls import path

from . import views

urlpatterns = [
    path('new', views.new),
    path('show', views.show),
    path('edit/<int:id>', views.edit),
    path('update/<int:id>', views.update),
    path('delete/<int:id>', views.delete),
]
