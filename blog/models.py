from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.
class Posts(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(null=True)
    date_posted = models.DateTimeField(default=timezone.now)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)

class Comments(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post_connected = models.ForeignKey(Posts, on_delete=models.CASCADE)
    content = models.TextField(max_length=150)
    date_posted = models.DateTimeField(default=timezone.now)

class Preference(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    post= models.ForeignKey(Posts, on_delete=models.CASCADE)
    value= models.IntegerField()
    date= models.DateTimeField(auto_now= True)

    def __str__(self):
        return str(self.user) + ':' + str(self.post) +':' + str(self.value)

    class Meta:
       unique_together = ("user", "post", "value")
