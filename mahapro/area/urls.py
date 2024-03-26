from django.urls import path
from .views import create_view, show_view, update_view, cancel_view

urlpatterns = [
    path('create/', create_view, name="create_url"),
    path('show/', show_view, name="show_url"),
    path('update/<int:pk>/', update_view, name="update_url"),
    path('cancel/<int:pk>/', cancel_view, name="cancel_url"),
]