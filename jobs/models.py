from django.db import models
from accounts.models import UserProfile, StudentProfile, Skill

class Compensation(models.Model):
    CHOICES = (
        ('0', 'ELO'),
        ('1', 'Volunteer'),
        ('2', 'Credit'),
        ('3', 'Direct Funding'),
        ('4', 'Sponsored Funding'),
        )
    name = models.CharField(max_length=50, choices=CHOICES)

    def __str__(self):
        return self.name

class Job(models.Model):
    # django has lots of different type of model fields
    # Had differenet required fields - max chars, digits etc 
    # Default for text feilds - already filled
    #Blank=False --- required field
    #null=False -- databasa
    created_by = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    title = models.CharField(max_length=200,blank=False) # set a max
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

    requirements = models.ManyToManyField(Skill,blank=False,related_name='requirements') #list from skill tags
    preferences = models.ManyToManyField(Skill,blank=False,related_name='preferences') # list from skill tags
    
    is_active = models.BooleanField(default = True)

    student_has_swiped = models.ManyToManyField(StudentProfile, related_name='student_has_swiped')
    students_who_swiped_yes = models.ManyToManyField(StudentProfile,related_name='students_who_swiped_yes')

    students_accepted_by_recruiter = models.ManyToManyField(StudentProfile,related_name='students_accepted_by_recruiter')
    students_in_maybe_pile = models.ManyToManyField(StudentProfile,related_name='students_in_maybe_pile_for_job')
    temp_maybe_list = models.ManyToManyField(StudentProfile,related_name='temp_maybe_list_for_job')

    recruiter_has_swiped = models.ManyToManyField(StudentProfile, related_name='recruiter_has_swiped_for_job')

    compensation_types = models.ManyToManyField(Compensation)

    def __str__(self):
        return self.title