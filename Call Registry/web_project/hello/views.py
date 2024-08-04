from django.shortcuts import render
from .models import*
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,template_name="home.html")

def insert(request):
    name=request.POST["name"]
    number=request.POST["number"]
    date=request.POST["date1"]
    next_followup_date=request.POST["date2"]
    additional_data=request.POST["detail"]
    row=Submission.objects.all()
    flag=0
    for i in row:
        if(i.number==number and i.name!=name):
            flag=1
    if(flag==0):
     yaleit=Submission.objects.create(
            name=name,
            number=number,
            date=date,
            next_followup_date=next_followup_date,
            additional_data=additional_data
        )
     yaleit.save()
     row=Submission.objects.all()
     return render(request,"show.html",{"key1":row,"v":"a"})
    else:
        l="a"
        return render(request,"home.html",{"key":l,"name":name,"number":number,"date1":date,"date2":next_followup_date,"data":additional_data})
    # return render(request,template_name="show")

def search(request):
    name=request.POST["name"]
    row=Submission.objects.all()
    l=[]
    for i in row:
        if(i.name==name):
             l.append(i)
    return render(request,"show.html",{"key1":l,"v":"c"},)
def show(request):
    row=Submission.objects.all()
    return render(request,"show.html",{"key1":row,"v":"a"})
def order(request):
    row=Submission.objects.all().order_by('name')
    return render(request,"show.html",{"key1":row,"v":"c"})
def showpage(request):
    all_data = Submission.objects.all()
    return render(request,"show.html",{"key1":all_data})