
from polls.models import *
import os
from django.shortcuts import render, get_object_or_404
import random, string

finish_number_num = 1000
now_number_num = 0

def check_use(user_name):
    text_name = 'polls/utils/worker_id.txt'
    with open(text_name, 'r', encoding='utf8', errors='ignore') as f:
        lines = f.read().strip().split('\n')
        worker_list =  [worker_name for worker_name in lines]
    if user_name in worker_list:
        if Person.objects.filter(person=user_name).count() == 0:
            q = Person(person=user_name)
            q.save()
        return 1
    else:
        return 0

def get_workse_list():
    text_name = 'polls/utils/worker_id.txt'
    with open(text_name, 'r', encoding='utf8', errors='ignore') as f:
        lines = f.read().strip().split('\n')
        worker_list = [worker_name for worker_name in lines]
    return worker_list

def add_user(worker_id):
    if Person.objects.filter(person=worker_id).count() == 0:
        q = Person(person=worker_id)
        q.save()

def check_data_num(worker_id, num):
    worker_id_ori = worker_id.split('-')
    if len(worker_id_ori) <= 1:
        return 1
    else:
        worker_id_ori_name = worker_id_ori[0]
        person_data = Person.objects.all()
        for person in person_data:
            person_name = person.person
            if person_name == worker_id:
                continue
            person_name_ori = person_name.split('-')[0]
            if worker_id_ori_name == person_name_ori:
                person_query = get_object_or_404(Person, person=person_name)
                dir_num_pre = PersonDirectory.objects.get(person=person_query).dir_num.dir_num
                if dir_num_pre == num:
                    return 0
        return 1

def check_data_full(dir_name, i):
    dir_name_data = get_object_or_404(Directory, dir_name=dir_name)
    dir_num_data = get_object_or_404(DirNum, dir_name=dir_name_data, dir_num=i)
    q = DirFinFlg.objects.get(dir_num=dir_num_data)
    flg = q.fin_flg
    return flg

def get_personn_dir_num(dir_count, worker_id, dir_name):
    global finish_number_num, now_number_num

    dir_num = 0
    dir_name_data = get_object_or_404(Directory, dir_name=dir_name)
    dir_num_data = get_object_or_404(DirNum, dir_name=dir_name_data, dir_num=0)
    count_person = PersonDirectory.objects.filter(dir_num=dir_num_data).count()

    if count_person < 5 and check_data_num(worker_id, dir_num):
        check_flg = 0
    else:
        check_flg = 1
        count_person = 5

    for i in range(dir_count):
        if check_data_full(dir_name, i):
            continue
        dir_num_data = get_object_or_404(DirNum, dir_name=dir_name_data, dir_num=i)
        count_person_i = PersonDirectory.objects.filter(dir_num=dir_num_data).count()
        if count_person_i < count_person and check_data_num(worker_id, i):
            count_person = count_person_i
            dir_num = i
            check_flg = 0

    if check_flg == 0:
        now_number_num += 1

    if now_number_num > finish_number_num:
        dir_num = -1
    elif check_flg:
        dir_num = -2

    return dir_num

def get_person_dir(worker_id, dir_name):
    # print("./templates/{}/".format(dir_name))
    path, dirs, files = next(os.walk("./templates/{}/".format(dir_name)))
    dir_count = len(dirs)

    person = get_object_or_404(Person, person=worker_id)

    fincode = make_fincode(10)

    if PersonDirectory.objects.filter(person=person).count() == 0:
        dir_num = get_personn_dir_num(dir_count, worker_id, dir_name)
        dir_name_data = get_object_or_404(Directory, dir_name=dir_name)
        dir_num_data = get_object_or_404(DirNum, dir_name=dir_name_data, dir_num=dir_num)

        q = PersonDirectory(person=person, dir_num=dir_num_data)
        q.save()
        q = FinishCode(person=person, code=fincode)
        q.save()
    else:
        q = PersonDirectory.objects.get(person=person)
        dir_num_data = q.dir_num
        dir_num = dir_num_data.dir_num

    return dir_num


def make_fincode(n):
   return ''.join(random.choices(string.ascii_letters, k=n))

def get_dummycode(penalty):
    n = 9
    code = ''.join(random.choices(string.digits, k=n))
    code += str(penalty)
    return code

def get_fincode(worker_id):
    person = get_object_or_404(Person, person=worker_id)
    q = FinishCode.objects.get(person=person)
    fincode = q.code
    return fincode