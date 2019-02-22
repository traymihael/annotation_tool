from django.urls import path
from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^index', views.index, name='index'),
    url(r'^annotation_start/', views.annotation_start, name='annotation_start'),
    url(r'^annotation/', views.annotation, name='annotation'),
    url(r'^input_worker_id/', views.input_worker_id, name='input_worker_id'),
    url(r'^guideline/', views.guideline, name='guideline'),
    url(r'^ful_text/', views.ful_text, name='ful_text'),
    url(r'^annotation_finish/', views.annotation_finish, name='annotation_finish'),
    url(r'^view_guideline/', views.view_guideline, name='view_guideline'),
    url(r'^delete_extra_person/', views.delete_extra_person, name='delete_extra_person'),
    url(r'^change_limit_num/', views.change_limit_num, name='change_limit_num'),
    url(r'^process_change_limit/', views.process_change_limit, name='process_change_limit'),
]