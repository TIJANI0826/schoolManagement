from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver 

from django.db import models
import calendar
from datetime import date, datetime, timedelta
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.forms import UserCreationForm
# Create your models here.
GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female')
)

MONTHS_CHOICE = (
    ('1', 'January'),
    ('2', 'February'),
    ('3', 'March'),
    ('4', 'April'),
    ('5', 'May'),
    ('6', 'June'),
    ('7', 'July'),
    ('8', 'August'),
    ('9', 'September'),
    ('10', 'October'),
    ('11', 'November'),
    ('12', 'December')
)
def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.admission_no, filename)

class Course(models.Model):
    course_name = models.CharField(max_length=255)
    course_id = models.CharField(max_length=255)

    description = models.TextField(max_length=1000)

    def __str__(self):
        return  self.course_name
    
    # def get_absolute_url(self):
    #     return reverse('course_update', kwargs={'pk': self.pk})



class Student(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    admission_no = models.IntegerField(unique=True)
    date_of_admission = models.DateField()
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    date_of_birth = models.DateField()

    address = models.CharField(max_length=150, default="Not Set")
    is_studying = models.BooleanField(default=True)
    current_class = models.ManyToManyField(Course)
    profile_image = models.ImageField(upload_to='gallery', blank=True)

    def full_name(self):
        return '{} {}'.format(self.first_name, self.last_name).capitalize()

    full_name.admin_order_field = 'first_name'

    @property
    def detail(self):
        return '{} Class - {}'.format(self.current_class, self.full_name)

    def __str__(self):
        return self.full_name()
    
    #related_course = models.ModelMultipleChoiceField(widget=models.CheckboxSelectMultiple,queryset=Course.objects.all(),required=False)

class Profile(models.Model):
    STUDENT = 1
    TEACHER = 2
    SUPERVISOR = 3
    ROLE_CHOICES = (
        (STUDENT,'Student'),
        (TEACHER,'Teacher'),
        (SUPERVISOR,'Supervisor')
    )


    user = models.OneToOneField(User,on_delete=models.CASCADE)
    bio = models.TextField(max_length=500,blank=True)
    location = models.CharField(max_length=30,blank=True)
    birth_date = models.DateField(null=True,blank=True)
    roles = models.PositiveSmallIntegerField(choices=ROLE_CHOICES,null=True,blank=True)
    admission_no = models.IntegerField(unique=True,null=True)
    date_of_admission = models.DateField(null=True,blank=True)

    gender = models.CharField(max_length=1, choices=GENDER_CHOICES,null=True)
    address = models.CharField(max_length=150, default="Not Set")
    is_studying = models.BooleanField(default=False)
    course = models.ManyToManyField(Course)
    profile_image = models.ImageField(upload_to=user_directory_path, blank=True)

    def full_name(self):
        return '{} {}'.format(self.first_name, self.last_name).capitalize()

    full_name.admin_order_field = 'first_name'

    @property
    def detail(self):
        return '{} Class - {}'.format(self.current_class, self.full_name)
    def __str__(self):
        return '%s' % self.user

@receiver(post_save,sender=User)
def create_user_profile(sender,instance,created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
@receiver(post_save,sender=User)
def save_user_profile(sender,instance,**kwargs):
    instance.profile.save()

# @receiver(post_save,sender=User)
# def create_user_course(sender,instance,created,**kwargs):
#     if created:
#         Course.objects.create(user=instance)
# @receiver(post_save,sender=User)
# def save_user_course(sender,instance,created,**kwargs):
#     instance.course.save()
