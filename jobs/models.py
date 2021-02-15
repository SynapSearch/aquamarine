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
    CatagoryType = (('1', 'Course 1'),
                    ('2','Course 2'),
                    ('3', 'Course 3'),
                    ('4', 'Course 4'),
                    ('5', 'Course 5'),
                    ('6', 'Course 6'),
                    ('7', 'Course 7'),
                    ('8','Course 8'),
                    ('9', 'Course 9'),
                    ('10', 'Course 10'),
                    ('11', 'Course 11'),
                    ('12', 'Course 12'),
                    ('14', 'Course 14'),
                    ('15', 'Course 15'),
                    ('15', 'Course 16'),
                    ('17', 'Course 17'),
                    ('18', 'Course 18'),
                    ('20', 'Course 20'))
    catagory = models.CharField(blank=True, max_length = 10, choices = CatagoryType),
    TermType = (('Summer', 'summer'),
            ('Fall', 'fall'),
            ('IAP', 'iap'),
            ('Spring', 'spring'))
    term = models.CharField(blank=True, choices = TermType, max_length = 10) # select from drop down
    RequirmentsList = (('C++','c++'),
                        ('Research', 'research'),
                        ('Python','python'),
                        ('MatLab','matlab'),
                        ('3D Printing','3d printing'))
    requirments = models.CharField(blank = True, choices = RequirmentsList, max_length = 20)#list from skill tags
    prefences = models.CharField(blank = True, choices = RequirmentsList, max_length = 20)# list from skill tags
    
    ACTIVE = 'active'
    ARCHIVED = 'archived'

    CHOICES_STATUS = (
        (ACTIVE, 'Active'),
        (ARCHIVED, 'Archived')
    )
    status = models.CharField(max_length=20, choices=CHOICES_STATUS, default=ACTIVE)
    def __str__(self):
        return self.title