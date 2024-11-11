from django.shortcuts import render,redirect
from django.views import View
from .forms import TaskForm
from django.http import HttpResponse
from .models import task

# Create your views here.
# def landingView(request):
#     return render(request,'landing.html')

class LandingView(View):
    def get(self,request):
        return render(request,'landing.html')

# def DashboardView(request):
#     return render(request,'dashboard.html')

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


