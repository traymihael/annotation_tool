from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
# from rest_framework.views import APIView
from polls.models import *
from django.utils import timezone
import os
import random

def add_data(request):
    candidate_len = int(request.POST.get('candidate_len'))
    target_word = request.POST.get('target')
    text = request.POST.get('text')
    person_name = request.POST.get('worker_id')
    index = request.POST.get('target_index')
    dir_name = request.POST.get('dir_name').split('/')[0]

    # person_name = 'Ashihara'

    target = get_object_or_404(Vocabulary, word=target_word)
    person = get_object_or_404(Person, person=person_name)
    text = get_object_or_404(Text, text=text)
    target_index = get_object_or_404(TargetIndex, text=text, target=target, index_num=index)
    dir_name = get_object_or_404(Directory, dir_name=dir_name)

    # print(candidate_len, person)


    for i in range(int(candidate_len)):
        candidate_word = request.POST.get('candidate_word{}'.format(i))
        candidate = get_object_or_404(Vocabulary, word=candidate_word)
        target_data = get_object_or_404(TargetData, target_index=target_index, candidate=candidate)
        result_data = request.POST.get('annotation_result{}'.format(i))
        comment = request.POST.get('comment{}'.format(i))
        # print(candidate_word, i)

        if Annotation.objects.filter(person=person, dir_name=dir_name, target_data=target_data).count():
            q = Annotation.objects.get(person=person, dir_name=dir_name, target_data=target_data)
            q.result = result_data
            q.comment = comment
            # print(result_data)
        else:
            q = Annotation(person=person, dir_name=dir_name, target_data=target_data, result=result_data, comment=comment)
        q.save()

def next_html(request, context):
    dir_name = request.POST.get('dir_name')
    file_num = int(request.POST.get('file_num'))

    path, dirs, files = next(os.walk("./templates/{}/".format(dir_name)))
    file_count = len(files)

    context['file_num_display'] = str(file_num + 2)
    context['all_num'] = file_count

    # print(file_count, file_num)

    if file_count -1 == file_num:
        # path, dirs, files = next(os.walk("./templates/check_q/"))
        # file_count = len(files)
        # file_num = random.randint(0, file_count-1)
        # annotation_name = 'check_q/annotation{}.html'.format(file_num)

        annotation_name = 'finish.html'

    else:
        annotation_name = '{}/annotation{}.html'.format(dir_name, file_num + 1)
    return annotation_name, context


def get_page_data_start(dir_name, person_dir):
    path, dirs, files = next(os.walk("./templates/{}/annotation{}/".format(dir_name, person_dir)))
    file_count = len(files)
    return file_count

def check_ans(request):
    penalty = 0
    for i in range(3):
        result_data = int(request.POST.get('annotation_result{}'.format(i)))
        if result_data == 1:
            penalty += 1
        elif result_data == 2:
            penalty += 2
    return penalty
