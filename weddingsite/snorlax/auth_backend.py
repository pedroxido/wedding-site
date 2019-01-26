from django.contrib.auth.backends import ModelBackend
from .models import Person

class PasswordlessAuthBackend(ModelBackend):
	def authenticate(self, name=None):
		try:
			return Person.objects.get(full_name=name)
		except Person.DoesNotExist:
			return None

	def get_user(self, user_id):
		try:
			return Person.objects.get(pk=user_id)
		except Person.DoesNotExist:
			return None