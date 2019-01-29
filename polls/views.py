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
    # context['workse_list'] = user_management.get_workse_list()
    return render(request, 'input_worker_id.html', context)


def annotation_start(request):
    dir_name = 'cefr_lp_v2'
    context = {}
    worker_id = request.POST.get('worker_id')
    if worker_id == '':
        annotation_name = 'input_worker_id_error.html'
    else:
        context['worker_id'] = worker_id
        context['file_num_display'] = 1

        user_management.add_user(worker_id)
        person_dir = user_management.get_person_dir(worker_id, dir_name)

        if person_dir == -1:
            annotation_name = 'error_full.html'
        elif person_dir == -2:
            annotation_name = 'person_full.html'
        else:
            context['all_num'] = add_annotation_data.get_page_data_start(dir_name, person_dir)
            annotation_name = '{}/annotation{}/annotation0.html'.format(dir_name, person_dir)

    return render(request, annotation_name, context)


def annotation(request):
    context = {}
    worker_id = request.POST.get('worker_id')
    context['worker_id'] = worker_id

    add_annotation_data.add_data(request)
    annotation_name, context = add_annotation_data.next_html(request, context)

    context['fincode'] = user_management.get_fincode(worker_id)

    return render(request, annotation_name, context)

def guideline(request):
    context = {}
    annotation_name = 'guideline.html'

    return render(request, annotation_name, context)

def ful_text(request):
    context = {}
    annotation_name = 'ful_text.html'
    original_text = request.POST.get('dir_name')
    dir_name = request.GET.get('dir_name')
    print(request)
    print(original_text)
    print(dir_name)

    return render(request, annotation_name, context)

def annotation_finish(request):
    context = {}
    annotation_name = 'finish.html'
    # print(annotation_name)
    penalty = add_annotation_data.check_ans(request)
    worker_id = request.POST.get('worker_id')
    context['worker_id'] = worker_id
    if penalty < 2:
        context['fincode'] = user_management.get_fincode(worker_id)
    else:
        context['fincode'] = user_management.get_dummycode(penalty)

    return render(request, annotation_name, context)


