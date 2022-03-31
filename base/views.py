from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import Vendor
from django.contrib.auth import login,logout,authenticate
# Create your views here.

def home(request):
    
    vendors = Vendor.objects.all()
    return render(request,"base/home.html",{'vendors':vendors})

def signin(request):
   
    if request.method == 'POST':
        username = request.POST["username"]
        pass1 = request.POST["pass1"]

        user = authenticate(username = username,password = pass1)

        if user is not None:
            login(request,user)
            return redirect(home)

        else:
            print('error')
            return redirect(signin)

    
    return render(request,"base/signin.html")

def register(request): 
    if request.method == 'POST':
        username = request.POST["username"]
        fname = request.POST["name"]
        sname = request.POST["surname"]
        email = request.POST["email"]
        pass1 = request.POST["pass1"]
        pass2 = request.POST["pass2"]

        myuser = User.objects.create_user(username,email,pass1)
        myuser.first_name = fname
        myuser.last_name = sname

        myuser.save()

        return redirect('signin')

    return render(request,"base/register.html")
def vendor(request):
    if request.method == "POST":
        fname = request.POST["name"]
        sname = request.POST["surname"]
        phone_num = request.POST["phone"]
        item_name = request.POST["item_name"]
        item_img = request.POST["item_img"]
        item_price = request.POST["item_price"]
        item_type = request.POST["item_type"]

        v = Vendor(fname = fname,sname = sname,phone_num = phone_num ,item_name = item_name,item_img = item_img,item_price =item_price,item_type = item_type)
        v.save()
        return redirect("home")

    return render(request,"base/vendor.html")

def profile(request):
    user = request.user
    items_query = Vendor.objects.filter(fname = user)
    context = {"items_query":items_query}
    return render(request,"base/profile.html",context)


def signout(request):
    logout(request)
    return redirect('signin')