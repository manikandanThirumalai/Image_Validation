from django.shortcuts import render, redirect
from django.contrib.auth.models import auth
from .form import ImageForm
from django.db.models import Q
from .models import Image
from django.conf import settings
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.forms import UserCreationForm
from django.db import connections

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_user')
    else:
        form = UserCreationForm()
        return render(request, 'register.html', {'form': form})


@csrf_exempt
def login_user(request):
    db_name = connections['default'].settings_dict['NAME']
    db_user = connections['default'].settings_dict['USER']
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('display/')
    else:
        form = AuthenticationForm(request)

    return render(request, 'login.html', {'form': form})


def logout_user(request):
    auth.logout(request)
    return redirect("login_user")

def upload_image(request):
    data = Image.objects.all()
    context = {
        'data': data
    }
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES) 
        if form.is_valid():
          try:
            image_image=form.cleaned_data['image']
            image_title=form.cleaned_data['title']
            image_description=form.cleaned_data['description']
            image_category=form.cleaned_data['category']
            image_data=image_image.read()
            
            model = Image()
            model.title=image_title
            model.image=image_image
            model.description=image_description
            model.category=image_category
            model.image_data=image_data
            model.save()
            
            return render(request, settings.IMGPATH,context)
            
          except:
            pass
       
    else:
         form = ImageForm()
         
    return render(request, 'imageupload.html', {'form': form})

def display(request):
    data = Image.objects.all()
    context = {
        'data': data
    }
    return render(request, settings.IMGPATH, context)


def search_image(request):
    query = request.GET.get('q')
    images = Image.objects.filter(Q(image__icontains=query) | Q(title__icontains=query) | Q(description__icontains=query) | Q(category__icontains=query))
    context = {
        'data': images
    }
    return render(request, settings.IMGPATH, context)
