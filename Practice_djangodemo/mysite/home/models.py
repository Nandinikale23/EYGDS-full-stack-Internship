from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField( max_length=255)
    email=models.EmailField()
    phone=models.CharField(max_length=20)
    date=models.DateField()
    rollno = models.IntegerField(default=0)

    
    def __str__(self):
        return self.name
    
     
