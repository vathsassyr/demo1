from .views import *
from django.urls import path 


urlpatterns = [
       path('', home, name = 'home'),
       path('about/', about, name = 'about'),
       path('signup/', signupposts, name = 'signup'),
       path('login/', loginposts, name = 'login'),
       path('logout/', logoutposts, name = 'logout'),
       path('posts-display/', displayposts, name = 'posts-display'),
       path('add-posts/', addposts, name = 'add-posts'),
       path('updateposts/<int:id>', updateposts, name = 'updateposts'),
       path('deleteposts/<int:id>', deleteposts, name = 'deleteposts'),
]
