from django.db import models
from django.contrib.auth.models import User


# Create a Profile model by extending the default User model
class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	display_name = models.CharField(max_length=63)
	email_address = models.EmailField(max_length=200)

	# shows the owner's name instead of Profile object (1), Profile object (2), etc., 
	def __str__(self):
		return self.user.get_full_name() or self.user.username