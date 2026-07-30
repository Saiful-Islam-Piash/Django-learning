from django.db import models
from authors.models import Author
from category.models import Category

# Create your models here.
class Posts(models.Model):
    title=models.CharField( max_length=50)
    content=models.TextField()
    author=models.ForeignKey(Author,on_delete=models.CASCADE)
    category=models.ManyToManyField(Category)

    def __str__(self):
        return self.title
    
