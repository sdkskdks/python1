from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as LogIn
from django.contrib.auth import logout as LogOut
from django.shortcuts import render
from django.shortcuts import redirect
from .models import List

def signout(request):
    LogOut(request)
    return redirect(signin)

def signin(request):
    if request.method == 'POST':
        user = authenticate(request, username=request.POST['email'], password=request.POST['password'])
        LogIn(request, user)
        return redirect(index)
    return render(request, 'main/sign.html')

def signup(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('pass')
        user2 = User.objects.create_user(username=email,email=email, first_name=name,password=password)
        user2.save()
        user = authenticate(request, username=email, password=password)
        LogIn(request, user)
        return redirect('/')

def deleteItem(request, item_id):
    List.objects.get(id=item_id).delete()
    return redirect('/')

def add(request):
    if request.method == 'POST':
        id = request.user.id
        name = request.POST['name']
        new_item = List(title=name, user_id=id)
        new_item.save()
        return redirect('/')

def index(request):
    if not request.user.is_authenticated:
        return redirect(signin)
    id = request.user.id
    items = List.objects.filter(user_id=id)
    return render(request, 'main/index.html', {'items': items})