from django.db import models
from django.urls import reverse


class SubjectClass(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name



class Student(models.Model):
    name = models.CharField(max_length=128)
    s_class = models.ManyToManyField(SubjectClass)


    def __str__(self):
        return self.name

    def join_class_list(self):
        l = [c.name for c in self.s_class.all()]
        return l

    def get_delete_url(self):
        return reverse('student_delete',kwargs={'pk':self.pk})