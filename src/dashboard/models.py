from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

GENDER_CHOICES = (

('M', 'Male'),
('F', 'Female')

)

CONDITION_CHOICES = (

('A', 'Condition A'),
('B', 'Condition B'),
('C', 'Condition C'),
('D', 'Condition D'),

)
class EditProfile(models.Model):
    first_name = models.CharField(max_length=250)
    surname = models.CharField(max_length=500)
    gender = models.CharField(max_length=1,
                              choices=GENDER_CHOICES)
    date_of_birth = models.DateField()
    condition = models.CharField(max_length=1,
                              choices=CONDITION_CHOICES, null = True, blank=True)

    # def get_absolute_url(self):
    #     return reverse('music:detail', kwargs={'pk': self.pk})
    #
    # def __str__(self):
    #     return self.album_title + ' - ' + self.artist



class sampleTree(models.Model):
    tree_name = models.CharField(max_length=250)
    relations = models.CharField(max_length=10000)

class relationships(models.Model):

    key = models.AutoField(primary_key=True, blank = False)
    UserID = models.IntegerField(null = True, blank = True)
    name = models.CharField(max_length=500, blank = False)
    sex = models.CharField(max_length=1,
                              choices=GENDER_CHOICES, blank = False)
    mother = models.IntegerField(null = True, blank = True)
    father = models.IntegerField(null = True, blank = True)
    husband = models.IntegerField(null = True, blank = True)
    wife = models.IntegerField(null = True, blank = True)
    attribute = models.CharField(max_length=100,
                              choices=CONDITION_CHOICES, null = True, blank = True)
