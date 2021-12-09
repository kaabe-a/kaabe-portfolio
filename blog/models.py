from django.db import models
from django.conf import settings
from django.urls import reverse
User = settings.AUTH_USER_MODEL

STATUS_CHOICES = (
        ('Drafted','Drafted'),
        ('Published','Published'),
        ('Suspended','Suspended'),
    )

class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)
    image = models.ImageField(upload_to='post_images/', null=True,blank=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    body =  models.TextField('Editor',blank=True, null=True)
    status = models.CharField(max_length=56,choices=STATUS_CHOICES,default='drafted')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title
    
    def get_absolute_url(self,*args):
        return reverse('detail',args=[
            self.pk
        ])
        

