from django.db import models
from django.urls import reverse
# from django.contrib.auth.models import User



class Student(models.Model):
    first_name = models.CharField(("Student First Name"), max_length=50)
    last_name = models.CharField(("Student Last Name"), max_length=50)
    age = models.DateField(("Date Of Birth"), auto_now=False, auto_now_add=False)
    gender = models.CharField(("Student Gender"), max_length=10)
    address = models.CharField(("Student Address"),max_length=100)
    phone = models.BigIntegerField(("Parent Phone number"))
    admission_date = models.DateTimeField(("Student admission Date Time"), auto_now=False, auto_now_add=True)
    
    
    def __str__(self) -> str:
        return (f'self.first_name self.last_name')
    
    
    def get_absolute_url(self):
        return reverse('student-detail', kwargs={'pk': self.pk})
    
    
    class Meta:
        ordering = ['-admission_date']
    