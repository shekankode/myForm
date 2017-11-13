from __future__ import unicode_literals

from django.db import models

# Create your models here.

class FormList(models.Model):
    pass

class FormHeader(models.Model):
    form_title = models.CharField(max_length=100)
    form_description = models.TextField()
    formNo = models.ForeignKey(FormList,default=0)
    #formNo=models.IntegerField()
class Questions(models.Model):
    ques=models.TextField()
    formNo = models.ForeignKey(FormList,default=0)
    # formNo=models.IntegerField()
    # quesNo=models.IntegerField()
    def __str__(self):
        return "{0}".format(self.ques)

class Answers(models.Model):
    fieldType=models.TextField()
    question=models.ForeignKey(Questions,default="0")
    ans=models.TextField(default=0)
    # formNo=models.IntegerField()
    # quesNo=models.ForeignKey()


#class FormList(models.Model):
