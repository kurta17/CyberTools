from django.db import models

class PasswordEntry(models.Model):
    hashed_password = models.CharField(max_length=128)  # Adjust max_length as needed
    created_at = models.DateTimeField(auto_now_add=True)

    
