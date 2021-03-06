from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _


RSVP_STATUS = (
	('CONFIRMED', _('Accept')),
	('DECLINED', _('Decline'))
)

MEAL_OPTIONS = (
	('MEAL_1', _('Meal Option 1')),
	('MEAL_2', _('Meal Option 2')),
	('MEAL_3', _('Meal Option 3')),
	('MEAL_4', _('Meal Option 4')),
	('MEAL_5', _('Meal Option 5')),
	('MEAL_6', _('Meal Option 6')),
	('MEAL_7', _('Meal Option 7')),
)

class Person(models.Model):
	full_name = models.CharField(max_length=100, verbose_name=_('full name'))
	email = models.EmailField(max_length=254, blank=True, verbose_name=_('email'))
	last_login = models.DateTimeField(default=timezone.now)
	status = models.CharField(max_length=9, choices=RSVP_STATUS, verbose_name=_('status'), default='DECLINED')
	meal = models.CharField(max_length=20, choices=MEAL_OPTIONS, verbose_name=_('meal options'), default='MEAL_1')
	notes = models.TextField(blank=True, verbose_name=_('dietary restrictions'))
	rsvp_date = models.DateTimeField(blank=True, null=True, verbose_name=_('RSVP date'))

	def __str__(self):
		return self.full_name

	@property
	def is_authenticated(self):
		return True

class FamilyGroup(models.Model):
	created_date = models.DateTimeField(default=timezone.now, verbose_name=_('creation date'))
	member = models.ManyToManyField(Person, verbose_name=_('full name'))

	def __str__(self):
		return str(self.id)

