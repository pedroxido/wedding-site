from django import forms
from .models import Person
from django.contrib.auth import authenticate
from django.utils.translation import ugettext_lazy as _

class PersonForm(forms.ModelForm):

	class Meta:
		model = Person
		fields = ('full_name',)
		widgets = {
			'full_name' : forms.TextInput(
				attrs={
					'class':'form-control',
					'placeholder': 'Your Name*'
				}
			)
		}

	def clean_full_name(self):
		full_name = self.cleaned_data['full_name']
		person = authenticate(name=full_name)
		if person is None:
			raise forms.ValidationError(_("Oops! We are having trouble finding your invite. Please try another spelling of your name or contact the couple"))
		return full_name

class RSVPForm(forms.ModelForm):

	class Meta:
		model = Person
		fields = ('status', 'meal', 'notes', 'full_name', 'id')
		labels = {
            'status': _('Will you go?'),
        }
		widgets = {
			'id' : forms.HiddenInput(
				attrs={
				'class' : 'hidden-id'
				}
			), 'full_name' : forms.HiddenInput(
				attrs={
				'class' : 'hidden-full-name'
				}
			), 'status' : forms.Select(
				attrs={
					'class':'form-control',
				},
			), 'meal' : forms.Select(
				attrs={
					'class':'form-control',
				}
			), 'notes' : forms.Textarea(
				attrs={
					'class':'form-control',
				}
			),
		}

