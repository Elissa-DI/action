from django.urls import path
from . import views

urlpatterns = [
    path("blogs/", views.index, name="index"),
    path("blogs/<int:id>/", views.index_id, name="index_id"),
    path("blogs/<str:title>/", views.index_title, name="index_title"),
]
