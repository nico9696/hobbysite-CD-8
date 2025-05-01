from django.db import models
from django.contrib.auth.models import User


# Create a Profile model by extending the default User model
class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	display_name = models.CharField(max_length=63)
	email_address = models.EmailField(max_length=200)