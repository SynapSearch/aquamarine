from django.db import models
from accounts.models import UserProfile, Skill

class Job(models.Model):
    # django has lots of different type of model fields
    # Had differenet required fields - max chars, digits etc 
    # Default for text feilds - already filled
    #Blank=False --- required field
    #null=False -- databasa
    created_by = models.ForeignKey(UserProfile, related_name='jobs', on_delete=models.CASCADE)
    title = models.TextField(blank=False) # set a max
    description = models.TextField(blank=False) # set a max words 
    published = models.DateField(auto_now_add = True)
    is_remote = models.BooleanField(default = False)

    courses = [1,2,3,4,5,6,7,8,9,10,11,12,14,15,16,17,18,20,21,22,24]
    CategoryType = tuple([(str(c), "Course " + str(c)) for c in courses])
    category = models.CharField(blank=True, max_length = 10, choices = CategoryType),

    TermType = (('0', 'Summer'),
            ('1', 'Fall'),
            ('2', 'IAP'),
            ('3', 'Spring'))
    term = models.CharField(blank=True, choices = TermType, max_length = 10) # select from drop down

    requirements = models.ManyToManyField(Skill,blank=False, related_name='requirements') #list from skill tags
    preferences = models.ManyToManyField(Skill,blank=False,related_name='preferences') # list from skill tags
    
    is_active = models.BooleanField(default = True)

    def __str__(self):
        return self.title