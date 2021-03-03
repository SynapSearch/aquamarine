from django.db import models
from accounts.models import UserProfile

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
    location = models.TextField(blank=True) # location look up?
    courses = [1,2,3,4,5,6,7,8,9,10,11,12,14,15,16,17,18,20,21,22,24]
    CategoryType = tuple([(str(c), "Course " + str(c)) for c in courses])
    category = models.CharField(blank=True, max_length = 10, choices = CategoryType),
    TermType = (('Summer', 'summer'),
            ('Fall', 'fall'),
            ('IAP', 'iap'),
            ('Spring', 'spring'))
    term = models.CharField(blank=True, choices = TermType, max_length = 10) # select from drop down
    RequirementsList = (('C++','c++'),
                        ('Research', 'research'),
                        ('Python','python'),
                        ('MatLab','matlab'),
                        ('3D Printing','3d printing'))
    requirements = models.CharField(blank = True, choices = RequirementsList, max_length = 20)#list from skill tags
    preferences = models.CharField(blank = True, choices = RequirementsList, max_length = 20)# list from skill tags
    
    ACTIVE = 'active'
    ARCHIVED = 'archived'

    CHOICES_STATUS = (
        (ACTIVE, 'Active'),
        (ARCHIVED, 'Archived')
    )
    status = models.CharField(max_length=20, choices=CHOICES_STATUS, default=ACTIVE)
    def __str__(self):
        return self.title