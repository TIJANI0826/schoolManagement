from django.shortcuts import render,redirect
from .forms import ProfileForm,UserForm
from django.db import transaction
from .models import User,Student ,Course,Profile
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from school.decorators import student_required
from django.contrib import messages
from django.views.generic.list import ListView
#Create your views here.

def index(request):
    return render(request,'index.html')

@login_required
@transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST,instance=request.user)
        profile_form = ProfileForm(request.POST,instance=request.user.profile)
        print(request.user.profile.roles)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request,('Your profile was successfully updated'))
            return redirect('index')
        else:
            messages.error((request,('Please correct the error below.')))
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
        return render(request,'profiles/profile.html',{'user_form': user_form,'profile_form':profile_form})
class CourseListView(ListView):
    model = Course
    paginate_by = 5