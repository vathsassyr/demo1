from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def signupposts(request):

    context = { 'error' : '' }

    if request.method == 'POST':
        user_check = User.objects.filter(username = request.POST['username'])
        
        if user_check.exists():
            context = { 'error': 'username already exists' }
            
            return render(request, 'signup.html', context)
        
        else:
            new_user = User(username = request.POST['username'],first_name = request.POST['first-name'],
                            last_name = request.POST['last-name'],
                            email = request.POST['email'],
                            age = request.POST['age'])
            
            new_user.set_password(request.POST['password'])
            new_user.save()
            
            return redirect('/login')

    return render(request, 'signup.html', context)    
        

def loginposts(request):

    context = { 'error' : '' }

    if request.method == 'POST':

        p = authenticate(username = request.POST['username'], password = request.POST['password'])

        if p:
            login(request, p)
            
            return redirect('/posts-display/')
        else:
        
            context = { 'error' : 'invalid credentials' }

            return render(request, 'login.html', context)
    
    return render(request, 'login.html', context)

@login_required(login_url = '/login')
def logoutposts(request):
    logout(request)
    return redirect('/')


@login_required(login_url = '/login')
def displayposts(request):
    posts = Post.objects.filter(user = request.user)
    context = { 'posts' : posts }
    return render(request, 'posts/posts-display.html', context)



@login_required(login_url = '/login')
def addposts(request):
    context = { 'posts1' : Post_Form() }

    if request.method == 'POST':
        post_form = Post_Form(request.POST)
        if post_form.is_valid():
            post = post_form.save(commit = False)
            post.user = request.user
            post.save()
            return redirect('/posts-display')
    
    return render(request, 'posts/add-posts.html', context)    


@login_required(login_url = '/login')
def updateposts(request, id):
    post = get_object_or_404(Post, id = id, user = request.user)

    if request.method == 'POST':
        post_form = Post_Form(request.POST, instance = post)
        if post_form.is_valid():
            post_form.save()
            return redirect('/posts-display')
    context = { 'posts1' : Post_Form(instance = post) }    
    return render(request, 'posts/add-posts.html', context)   



@login_required(login_url = '/login')
def deleteposts(request, id):
    post = get_object_or_404(Post, id = id, user = request.user)
    post.delete()
    return redirect('/posts-display')





           
            


"""from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate



def home(request):
    return render(request, 'home.html')



def about(request):
    return render(request, 'about.html')



def signupposts(request):
    context = { 'error' : '' }

    if request.method == 'POST':
        user_check = User.objects.filter(username = request.POST['username'])
        if user_check.exists():
            context = { 'error' : 'username already exists' }
            return render(request, 'signup.html', context)
        else:
            new_user = User(username = request.POST['username'],
                            first_name = request.POST['first-name'],
                            last_name = request.POST['last-name'],
                            email = request.POST['email'],
                            age = request.POST['age'])
            new_user.set_password(request.POST['password'])
            new_user.save()
            return redirect('/login')
    return render(request, 'signup.html', context)

def loginposts(request):
    context = { 'error' : '' }

    if request.method == 'POST':
        p = authenticate(username = request.POST['username'], password = request.POST['password'])
        if p:
            login(request, p)
            return redirect('/posts-display')
        else:
            context = { 'error' : 'invalid credentials' }
            return render(request, 'login.html', context) 
    
    return render(request, 'login.html', context)

login_required(login_url = '/login')
def logoutposts(request):
    logout(request)
    return redirect('/')

@login_required(login_url = '/login')
def displayposts(request):
    posts = Post.objects.filter(user = request.user)
    context = { 'posts' : posts }
    return render(request, 'posts/posts-display.html', context)

@login_required(login_url = '/login')
def addposts(request):
    context = { 'posts1' : Post_Form() }

    if request.method == 'POST':
        post_form = Post_Form(request.POST)
        if post_form.is_valid():
            post = post_form.save(commit = False)
            post.user = request.user
            post.save()
            return redirect('/posts-display')
    
    return render(request, 'posts/add-posts.html', context)    


login_required(login_url = '/login')
def updateposts(request, id):
    post = get_object_or_404(Post, user = request.user, id = id)
    context = { 'posts1' : Post_Form(instance = post) }

    if request.method == 'POST':
        p2 = Post_Form(request.POST, instance = post)
        if p2.is_valid():
            p2.save()
            return redirect('/posts-display')
    return render(request, 'posts/add-posts.html', context)
    
    
    

login_required(login_url = '/login')
def deleteposts(request, id):
    post = get_object_or_404(Post, id = id, user = request.user)    
    post.delete()
    return redirect('/posts-display')"""





