from django.shortcuts import render ,HttpResponse,redirect
from .models import Pizza
from custompizza.forms import createpizza


# Create your views here.
def home(request):
    return render(request,"home.html")

def show(request):
    pizzas=Pizza.objects.all()
    return render(request,"show.html",{'pizzas':pizzas})

def create(request):
    if request.POST:
        print("HOOO")
        form=createpizza(request.POST)
        print("After form")
        if form.is_valid():

            size=form.cleaned_data.get("size")
            print("hello",size)
            form.save()
            print("Bye")
            return render(request,"success.html")
        else:
            print("ELSE:")
            return render(request,"create.html",{'form':form})
    else:
        print("LAST ELSE")
        form=createpizza(None)
        return render(request,'create.html',{'form':form})
