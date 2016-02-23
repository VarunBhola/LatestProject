from django.db import models
from django.contrib.auth.models import (
AbstractBaseUser
)



class ArticleUser(AbstractBaseUser):
#     email = models.EmailField(
#         verbose_name='email address',
#         max_length=255,
#         unique=True,
#     )
    date_of_birth = models.DateField(blank=True,null=True)
    fb_id=models.CharField(max_length= 200,blank=True,null=True)
    google_id=models.CharField(max_length= 200,blank=True,null=True)
    linkedin_id=models.CharField(max_length= 200,blank=True,null=True)
    device_token=models.TextField(blank=True,null=True)
    device_type=models.IntegerField(default=1)
    create_date = models.DateTimeField(auto_now_add=True)
    change_date = models.DateTimeField(auto_now=True)

    def __unicode__(self):              # __unicode__ on Python 2
        return self.email

class Article(models.Model):
    name=models.CharField(max_length=200)
    desc=models.TextField()
    user=models.ForeignKey(ArticleUser)