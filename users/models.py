from django.db import models

# Create your models here
from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    USER_TYPES = (
        ('super_admin', 'Super Admin'),
        ('teacher', 'Teacher'),
        ('brand_leader', 'Brand Leader'),
        ('seo_specialist', 'SEO Specialist'),
        ('content_writer', 'Content Writer'),
        ('social_media_manager', 'Social Media Manager'),
        ('customer_service', 'Customer Service'),
        ('data_analyst', 'Data Analyst'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=50, choices=USER_TYPES, default='brand_leader')
    phone = models.CharField(max_length=15, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.user_type}"
