from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
# from rest_framework.views import APIView
from polls.models import *
from django.utils import timezone

from polls.utils import add_annotation_data, user_management

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def input_worker_id(request):
    context = {}
    context['workse_list'] = user_management.get_workse_list()
    return render(request, 'input_worker_id.html', context)


def annotation_start(request):
    context = {}
    worker_id = request.POST.get('worker_id')
    context['worker_id'] = worker_id

    if user_management.check_use(worker_id):
        annotation_name = 'test/annotation0.html'
    else:
        annotation_name = 'input_worker_id_error.html'

    return render(request, annotation_name, context)


def submit_data(request):
    context = {}
    worker_id = request.POST.get('worker_id')
    context['worker_id'] = worker_id

    add_annotation_data.add_data(request)
    annotation_name = add_annotation_data.next_html(request)

    return render(request, annotation_name, context)

