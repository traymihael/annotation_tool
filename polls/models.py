import datetime
from django.db import models
from django.utils import timezone



class Text(models.Model):
    text = models.CharField(max_length=300)

class Vocabulary(models.Model):
    word = models.CharField(max_length=20)

class Person(models.Model):
    person = models.CharField(max_length=20)

class TargetIndex(models.Model):
    text = models.ForeignKey(Text, on_delete=models.CASCADE)
    target = models.ForeignKey(Vocabulary, on_delete=models.CASCADE)
    index = models.IntegerField(default=-1)

class TargetData(models.Model):
    target_index = models.ForeignKey(TargetIndex, on_delete=models.CASCADE)
    candidate = models.ForeignKey(Vocabulary, on_delete=models.CASCADE)

class Annotation(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    target_data = models.ForeignKey(TargetData, on_delete=models.CASCADE)
    result = models.IntegerField()
    comment = models.CharField(max_length=300)

