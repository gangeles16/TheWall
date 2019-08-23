from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
#remember to makemigrations to my specific app folder such as log_reg_app
def index(request):
    print(User.objects.all())
    return render(request,'index.html')

def register(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
    else:
        User.objects.create(
            first_name = request.POST['first_name'],
            last_name = request.POST['last_name'],
            email = request.POST['email'],
            password = request.POST['password'],
            confirm_password = request.POST['confirm_password'],
        )
    return redirect('/')

def login(request):
    errors = User.objects.login_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        request.session['id'] = User.objects.get(email=request.POST['login_email']).id
        print('////////////////////////////////////')
        print (request.session['id'])
        return redirect('/dashboard')
  
def dashboard(request):
    context = {
    "all_posts" : wall_post.objects.all().order_by("-created_at"),
    "all_comments" : Comment.objects.all()

    }
    print(context)
    return render(request,'dashboard.html', context)
    
    contents = {
        "all_comments" : Comments.objects.all()

    }
    print(contents)
    return render(request,'dashboard.html', contents)



def posting(request):
    user=User.objects.get(id=request.session['id'])
    wall_post.objects.create(
        wall_post = request.POST['wall_post'],
        user = user
    )
    return redirect('/dashboard')

def Comments(request):
    print('[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[')
    print(request.POST)
    current_user=User.objects.get(id=request.session['id'])
    current_wall_post= wall_post.objects.get(id=request.POST['wall_post_id'])
    Comment.objects.create(
        text = request.POST['text'],
        creator = current_user,
        commented_wall_post = current_wall_post
    )
    print(Comment.objects.all())
    return redirect('/dashboard') 

def delete_comment(request, id):
    c = Comment.objects.get(id=id)
    c.delete()
    return redirect('/dashboard')    

def logout(request):
    if request.
    request.session.clear()
    return redirect('/')
