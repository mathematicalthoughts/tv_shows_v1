from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('shows_new',views.createShows),
    path('shows/<int:id>',views.readShows, name="readShow"),
    path('shows/<int:id>/edit',views.editShows, name="editShow"),
    
]