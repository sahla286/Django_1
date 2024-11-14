from django.shortcuts import render,redirect
from django.views import View
from .forms import TaskForm,LoginForm,RegistrationForm
from django.http import HttpResponse
from .models import task
from django.contrib.auth import authenticate

# Create your views here.
# def landingView(request):
#     return render(request,'landing.html')

class LoginView(View):
    def get(self,request):
        form=LoginForm()
        return render(request,'login.html',{'form':form})
    def post(self,request):
        formdata=LoginForm(data=request.POST)
        if formdata.is_valid():
            uname=formdata.cleaned_data.get('username')
            pswd=formdata.cleaned_data.get('password')
            user=authenticate(request,username=uname,password=pswd)
            if user:
                return redirect('landing')
            else:
                return redirect('login')
        return render(request,'login.html',{'form':formdata})
        
class RegistrationView(View):
    def get(self,request):
        form=RegistrationForm()
        return render(request,'registration.html',{'form':form})
    def post(self,request):
        formdata=RegistrationForm(data=request.POST)
        if formdata.is_valid():
            formdata.save()
            return redirect('login')
        return render(request,'registration.html',{'form':formdata})

class LandingView(View):
    def get(self,request):
        return render(request,'landing.html')

class DashboardView(View):
    def get(self,request):
        data=task.objects.all()
        return render(request,'dashboard.html',{'data':data})
    
class AddView(View):
    def get(self,request):
        form=TaskForm()
        return render(request,'add.html',{'form':form})
    
    def post(self, request):
        form_data = TaskForm(data=request.POST)
        if form_data.is_valid():
            title = form_data.cleaned_data.get('title')
            desc = form_data.cleaned_data.get('description')
            date = form_data.cleaned_data.get('date')
            time = form_data.cleaned_data.get('time')
            task.objects.create(title=title, desc=desc, date=date, time=time)
            return redirect('dash')
        return render(request, 'addwork.html', {'form': form_data})

class DeleteTaskView(View):
    def get(self,request,*args,**kw):
        tid=kw.get('id')
        tk=task.objects.get(id=tid)
        tk.delete()
        return redirect('dash')
    

class EditTaskView(View):
    def get(self,request,**kw):
        tid=kw.get('id')
        tk=task.objects.get(id=tid)
        form=TaskForm(initial={'title':tk.title,'description':tk.desc,'date':tk.date,'time':tk.time})
        return render(request,'edit.html',{'form':form})
    def post(self,request,**kw):
        formdata=TaskForm(data=request.POST)
        tid=kw.get('id')
        tk=task.objects.get(id=tid)
        if formdata.is_valid():
            title = formdata.cleaned_data.get('title')
            desc = formdata.cleaned_data.get('description')
            date = formdata.cleaned_data.get('date')
            time = formdata.cleaned_data.get('time')
            tk.title=title
            tk.desc=desc
            tk.date=date
            tk.time=time
            tk.save()
            return redirect('dash')
        return render(request, 'edit.html', {'form': formdata})


