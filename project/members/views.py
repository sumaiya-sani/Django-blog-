from pyexpat import model
from sre_constants import SUCCESS
from django.shortcuts import get_object_or_404, render,redirect
from django.views import generic
from django.urls import reverse_lazy
from django.views.generic import DetailView
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth import authenticate,login,logout
from members.forms import SignUpForm,EditForm,LoginForm
from myblog.models import Profile


#class PasswordsChangeView(PasswordChangeView):
    #form_class=PasswordChangeView 
    #template_name='change_password.html'
    #success_url=reverse_lazy('myblog:home')

class UserProfileView(DetailView):
    model=Profile
    template_name='members_profile.html'

    def get_profile(self,*args,**kwargs):
        users=Profile.objects.all()
        context=super(UserProfileView,self).get_context_data(*args,**kwargs)
        page_user=get_object_or_404(Profile,id=self.kwargs['pk'])
        context['page_user']=page_user
        print(context)
        return context
        

          

class UserRegisterForm(generic.CreateView):
    form_class=SignUpForm 
    template_name='register.html'
    success_url=reverse_lazy('myblog:home')

class UserEditView(generic.CreateView):
    form_class=EditForm
    template_name='edit_profile.html'
    success_url=reverse_lazy('myblog:home')
    
#To find the user who login in and bring the profile of him 
    def get_object(self):
        return self.request.user

def login_page(request):
 if request.method=="POST":
    form=LoginForm()
    username=request.POST.get('username')
    password=request.POST.get('password')
    user=authenticate(request,username=username,password=password)
    if user is not None:
        login(request,user)
        return redirect('myblog:home')
    else:
        form=LoginForm()    
    
    return render(request,'login.html',{'form':form})      

# Create your views here.
