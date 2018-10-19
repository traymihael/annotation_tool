from django.urls import path
from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^index', views.index, name='index'),
    url(r'^annotation_start/', views.annotation_start, name='annotation_start'),
    url(r'^submit_data/', views.submit_data, name='submit_data'),
    url(r'^input_worker_id/', views.input_worker_id, name='input_worker_id'),
    url(r'^guideline/', views.guideline, name='guideline'),
    url(r'^ful_text/', views.ful_text, name='ful_text'),
]