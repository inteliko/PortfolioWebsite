from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100, default='General Inquiry')  
    message = models.TextField()

    def __str__(self):
        return self.name
