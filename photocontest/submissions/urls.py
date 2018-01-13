""" ------------------------------------------------------------------------------------------------------
    My code
------------------------------------------------------------------------------------------------------ """

from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index',),
    path('photos/', views.PhotoListView.as_view(), name='photos'),
    path('photo/<int:pk>', views.PhotoDetailView.as_view(), name='photo-detail'),
]

