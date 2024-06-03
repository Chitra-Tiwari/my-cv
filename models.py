from django.db import models

# Create your models here.
class candidate(models.Model):
    User_name=models.CharField(max_length=50)
    email_id=models.EmailField()
    phone=models.IntegerField()
    
    def __str__(self):
       return self.User_name
  