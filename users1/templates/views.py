from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.views import View


# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def posts(request):
    posts = Post.objects.all()
    return render(request, 'posts/posts-list.html', {'posts':posts})

def addposts(request):
    if request.method == 'POST':
        post_form = Post_Form(request.POST)
        if post_form.is_valid():
            post_form.save()

    return render(request, 'posts/posts-form.html', { 'posts': Post_Form() })

def displayposts(request):
    posts = Post.objects.all()
    context = { 'posts' : posts}
    return render(request, 'posts/posts-display.html', context)

def deleteposts(request, id):
    post = Post.objects.get(id=id)
    post.delete()
    return redirect('/posts-display/')

def updateposts(request, id):
    post = Post.objects.get(id=id)

    if request.method == 'POST':
        post_form = Post_Form(request.POST, instance = post)

        if post_form.is_valid():
            post_form.save()

        return redirect('/posts-display/') 

    return render(request, 'posts/posts-form.html', { 'posts' : Post_Form(instance=post) })   

def loginposts(request):

    context = {
        'error' : ''
    }

    if request.method == 'POST':
        
        user_exists = authenticate(username = request.POST['username'], password = request.POST['password'])

        if user_exists:
            login(request, user_exists)
            return redirect('/posts-display')
        else:
            context = {
                    'error' : 'invalid credentials'
                }
            return render(request, 'login.html', context)
            
        
    return render(request, 'login.html', context) 

def logoutposts(request):
    logout(request) 
    return redirect('/')

def signupposts(request):
    context = { 'error' : ''}

    if request.method == 'POST':
        user_check = User.objects.filter(username = request.POST['username'])
        if len(user_check) > 0:
            context = { 'error' : 'username already exists'}
            return render(request, 'signup.html', context)
        else:

            new_user = User(username = request.POST['username'], 
                            first_name = request.POST['first-name'],
                            last_name = request.POST['last-name'],
                            email = request.POST['email'],
                            age = request.POST['age'])

            new_user.set_password(request.POST['password'])

            new_user.save()

            return redirect('/login/')
        
    return render(request, 'signup.html', context)    
 



class Home(View):
    
    def get(self, request):
        return render(request, 'home.html') 


class About(View):
    
    def get(self, request):
        return render(request, 'about.html')


class Posts(View):
    
    def get(self, request):
        post = Post.objects.all()
        return render(request, 'posts/posts-list.html', { 'posts' : post })    


class AddPosts(View):
    
    def get(self, request):
        return render(request, 'posts/posts-form.html', { 'posts': Post_Form() })
    
    def post(self, request):
             post = Post_Form(request.POST)
             if post.is_valid():
                 post.save()
             return render(request, 'posts/posts-form.html', { 'posts' : Post_Form() })    


class DisplayPosts(View):

    def get(self, request):
        post = Post.objects.all()
        context = { 'posts' : post }
        return render(request, 'posts/posts-display.html', context)
    

class DeletePosts(View):

    def get(self, request, id):
        post = Post.objects.get( id = id ) 
        post.delete()   
        return redirect('/posts-display/')
    

class UpdatePosts(View):

    def get(self, request, id):
        post = Post.objects.get( id = id)
        return render(request, 'posts/posts-form.html', { 'posts' : Post_Form( instance = post ) })
    
    def post(self, request, id):
        post = Post.objects.get( id = id)
        post_form = Post_Form(request.POST, instance = post)
        if post_form.is_valid():
            post_form.save()
            return redirect('/posts-display/')
        

class LoginPosts(View):
    
    def get(self, request):
        context = { 'error' : ''}
        return render(request, 'login.html', context)

    def post(self, request):
                user = authenticate(username = request.POST['username'], password = request.POST['password'])
                if user:
                    login(request, user)
                    return redirect('/posts-display/')
                return render(request, 'login.html', { 'error' : 'invalid credentials' })
    

class LogoutPosts(View):
    
    def get(self, request):
        logout(request)
        return redirect('/')     
    

class SignUpPosts(View):
    
    def get(self, request):
        return render(request, 'signup.html', { 'error' : '' })

    def post(self, request):
            user_check = User.objects.filter(username = request.POST['username'])
            if len(user_check) > 0:
                context = { 'error' : 'username already exists'}
                return render(request, 'signup.html', context)
            else:
                new_user = User(username = request.POST['username'],
                                first_name = request.POST['first-name'],
                                last_name = request.POST['last-name'],
                                email = request.POST['email'],
                                age = request.POST['age'])
                new_user.set_password(request.POST['password'])
                new_user.save()
                return redirect('/login/')
            