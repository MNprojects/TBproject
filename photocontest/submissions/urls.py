""" ------------------------------------------------------------------------------------------------------
    My code
------------------------------------------------------------------------------------------------------ """
from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index',),
    path('photos/', views.PhotoListView, name='photos'),
    path('photo/<int:pk>', views.PhotoDetailView.as_view(), name='photo-detail'),
    path('signup/', views.signup, name='signup',),
    path('upload/', views.model_form_upload, name='upload',),
    path('contact/', views.contact, name='contact',),

]

