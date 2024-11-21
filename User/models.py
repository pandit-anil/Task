from django.db import models

class UserForm(models.Model):
    First_Name = models.CharField(max_length=20)
    Last_Name = models.CharField(max_length=20)
    Email = models.EmailField()
    Address = models.TextField()
    
    def __str__(self):
        return f'{self.First_Name}{self.Last_Name}'