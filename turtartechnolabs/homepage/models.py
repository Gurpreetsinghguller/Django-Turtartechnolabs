from django.db import models

# Create your models here.
class Contact(models.Model):
        name=models.CharField(default='',max_length=10)
        email=models.EmailField(default='',max_length=30)
        mobile_no = models.PositiveIntegerField(default='')
        date= models.DateTimeField(auto_now_add=True)
        message = models.TextField(default='')
        def __str__(self):
                return self.name
        
class Post(models.Model):

 
    sno =models.AutoField(primary_key=True)
    title=models.CharField(default='',max_length=100)
    sub_title=models.CharField(default='',max_length=70)
    content = models.TextField(default='')
    date= models.DateTimeField(auto_now_add=True,blank=True)
    
    image= models.ImageField(upload_to="images/",blank=True)
    def __str__(self):
        return self.title
    
        