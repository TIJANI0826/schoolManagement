from django import forms
from django.contrib.auth import get_user
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from .models import User,Student ,Course,Profile

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name','last_name','email')

class ProfileForm(forms.ModelForm):
    course = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple,queryset=Course.objects.all(),required=False)
    class Meta:
        model = Profile
        exclude = ['user']

class CourseForm(forms.ModelForm):
    course = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple,queryset=Course.objects.all(),required=False)
    #related_course = models.ModelMultipleChoiceField(widget=models.CheckboxSelectMultiple,queryset=Course.objects.all(),required=False)
    class Meta:
        model = Course
        exclude = ['course']