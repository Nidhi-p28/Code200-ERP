from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLE_CHOICES = (
        ('superadmin', 'Super Admin'),
        ('admin', 'College Admin'),
        ('staff', 'Staff'),
        ('student', 'Student'),
    )
    
    STAFF_TYPE_CHOICES = (
        ('teaching', 'Teaching Staff'),
        ('non_teaching', 'Non-Teaching Staff'),
    )
    
    BRANCH_CHOICES = (
        ('admission', 'Admission Branch'),
        ('examination', 'Examination Branch'),
        ('administration', 'Administration Branch'),
        ('hostel', 'Hostel Branch'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='student')
    staff_type = models.CharField(max_length=20, choices=STAFF_TYPE_CHOICES, blank=True, null=True)
    branch = models.CharField(max_length=50, choices=BRANCH_CHOICES, blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)

    def _str_(self):
        return f"{self.username} ({self.role})"

    def full_name(self):
        return f"{self.first_name} {self.last_name}"


 

    # College/Institution model
class College(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=50, unique=True)
    address = models.TextField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pincode = models.CharField(max_length=10)
    contact_email = models.EmailField()
    contact_phone = models.CharField(max_length=15)
    affiliation = models.CharField(max_length=100, blank=True, null=True)

    admin = models.OneToOneField(User, on_delete=models.CASCADE, related_name="college")

    def __str__(self):
        return self.name
    

