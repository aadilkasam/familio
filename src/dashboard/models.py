from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from datetime import date
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
('S', 'Deceased')

)

# database with data for sample tree
class sampleTree(models.Model):
    tree_name = models.CharField(max_length=250)
    relations = models.CharField(max_length=10000)


# relationships model containing all information about family members
class relationships(models.Model):

    key = models.AutoField(primary_key=True, blank = False)
    UserID = models.IntegerField(null = True, blank = True)
    name = models.CharField(max_length=500, blank = False)
    DOB = models.DateField(auto_now=False, auto_now_add=False, null = True, blank = True)
    sex = models.CharField(max_length=1,
                              choices=GENDER_CHOICES, blank = False)
    mother = models.IntegerField(null = True, blank = True)
    father = models.IntegerField(null = True, blank = True)
    husband = models.IntegerField(null = True, blank = True)
    wife = models.IntegerField(null = True, blank = True)
    smoker = models.BooleanField(default=False)
    attribute = models.CharField(max_length=10, null = True, blank = True)



    def __str__(self):
        return '{ key: %s, n: "%s", s: "%s", m: %s, f: %s, ux: %s, vir: %s, a: ["%s"] },' % (self.key, self.name, self.sex, self.mother, self.father, self.wife, self.husband, self.attribute)

    def get_absolute_url(self):
        return reverse('dashboard:member_update', kwargs={'id': self.key})
