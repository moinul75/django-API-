from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=100,blank=False)
    decription = models.TextField(blank=False)
    date = models.DateField(blank=False)
    Completed = models.BooleanField(blank=False)
    def __str__(self):
        return self.title
    
