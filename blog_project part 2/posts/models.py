from django.db import models
from django.contrib.auth.models import User
from category.models import Category

# Create your models here.
class Posts(models.Model):
    title=models.CharField( max_length=50)
    content=models.TextField()
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    category=models.ManyToManyField(Category)

    def __str__(self):
        return self.title
    
