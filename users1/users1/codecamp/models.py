"""from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    age = models.IntegerField(default = 0)



class Post(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    name = models.CharField(max_length = 100)
    description = models.TextField()
    date = models.DateField(auto_now_add = True)
    

    def __str__(self):
        return self.name"""



from django.db import models 
from django.contrib.auth.models import AbstractUser 

class User(AbstractUser):
    age = models.IntegerField(default = 0)


class Post(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    name = models.CharField(max_length = 100)
    description = models.TextField()
    date = models.DateField(auto_now_add = True)

    def __str__(self):
        return self.name    

