from django.db import models
from django.utils import timezone

class Person(models.Model):
	full_name = models.CharField(max_length=100)
	email = models.EmailField(max_length=254, blank=True)

	def __str__(self):
		return self.full_name

class FamilyGroup(models.Model):
	created_date = models.DateTimeField(default=timezone.now)
	member = models.ManyToManyField(Person)

	def __str__(self):
		return str(self.id)

RSVP_STATUS = (
	('CONFIRMED', 'Si Asistire'),
	('DECLINED', 'No Asistire')
)

MEAL_OPTIONS = (
	('MEAL_1', 'Meal Option 1'),
	('MEAL_2', 'Meal Option 2'),
	('MEAL_3', 'Meal Option 3')
)

class RSVP(models.Model):
	status = models.CharField(max_length=9, choices=RSVP_STATUS)
	meal = models.CharField(max_length=20, choices=MEAL_OPTIONS)
	notes = models.TextField(blank=True)
	rsvp_date = models.DateTimeField(default=timezone.now)
	person = models.OneToOneField(
		Person,
		on_delete=models.CASCADE,
		primary_key=True,
	)

	def __str__(self):
		return self.person.full_name