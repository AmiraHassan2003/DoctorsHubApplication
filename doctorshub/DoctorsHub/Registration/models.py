from django.db import models

class User(models.Model):
    userId = models.AutoField(primary_key=True)
    userName = models.CharField(max_length=50)
    userEmail = models.CharField(max_length=50)
    userPassword = models.CharField(max_length=50)
    isActive = models.BooleanField(default=True)

    def __str__(self):
        return self.userName

# Create your models here.
