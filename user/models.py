from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.core.validators import MinValueValidator, MaxValueValidator

class CustomUserManager(BaseUserManager):
    def create_superuser(self, email, password=None):
        user = self.model(email=email, is_staff=True, is_superuser=True)
        user.set_password(password)
        user.save()
        return user


class User(AbstractUser):
	"""docstring for User"""
	username			= None
	email 				= models.EmailField(verbose_name='Email Address', unique=True)
	name 				= models.CharField(max_length=50)
	contact_no 			= PhoneNumberField(blank=False, null=False, help_text='Add country code before the contact no.')
	USERNAME_FIELD 		= 'email' 
	friend              = models.ManyToManyField("User", related_name="userFriends", blank=True)
	user_permissions 	= None
	groups 				= None
	REQUIRED_FIELDS 	= []

	objects = CustomUserManager()
	

	def __str__(self):
		return self.email


class FriendRequest(models.Model):
	from_user	= models.ForeignKey(User, related_name="fromuser", on_delete=models.CASCADE)
	to_user 	= models.ForeignKey(User, related_name="to", on_delete=models.CASCADE)
	is_accepted 	= models.BooleanField(default=False)

