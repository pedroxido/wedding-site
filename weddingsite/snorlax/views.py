from django.shortcuts import render, redirect, get_object_or_404
from django.template import loader
from django.utils.translation import get_language
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.forms.models import model_to_dict
from django.db.models import F
from .forms import PersonForm, RSVPForm
from django.forms import modelformset_factory
from .models import  FamilyGroup, Person
import sys
from django import http

# Create your views here.
def render_rsvp(request):

	if request.user.is_authenticated :
		return redirect('user_login_rsvp')

	ctx = {}
	form = PersonForm(request.POST or None, request.FILES or None)
	ctx['form_name'] = 'person'

	if request.method == 'POST':
		try:
			if form.is_valid():
				group =	group_handler(form.cleaned_data['full_name'])
				print("group error!")
				if group is None:
					ctx['error_message'] = 'There is more than one "' + form.cleaned_data['full_name'] + '" on the guest list. Please contact Davide & Andrea to RSVP.'
					ctx['error_focus'] = 'PersonForm'
				else:
					ctx['person'] = authenticate(name=form.cleaned_data['full_name'])
					login(request, ctx['person'])

					return redirect('user_login_rsvp')
			else:
				ctx['error_focus'] = 'PersonForm'
		except Exception as e:
			if 'MultipleObjectsReturned' in type(e).__name__:
				ctx['error_message'] = 'There is more than one "' + form.cleaned_data['full_name'] + '" on the guest list. Please contact Davide & Andrea to RSVP.'
				ctx['error_focus'] = 'PersonForm'
			else:
				view_500(request, template_name='snorlax/500.html')
	
	ctx['form'] = form

	return render(request, 'snorlax/index_rsvp.html', ctx)

def group_handler(user):
	person_group_object = FamilyGroup.objects.filter(member__full_name=user)
	if person_group_object.count() > 1 :
		print("Error")
		return None
	group = FamilyGroup.objects.filter(pk=person_group_object[0].id)
	return group


@login_required(login_url='/' + get_language() + '/rsvp/#rsvp')
def render_auth_rsvp(request):
	ctx = {}

	if request.META.get('HTTP_REFERER') is None:
		ctx['form_name'] = 'rsvp'
	elif 'rsvp' in request.META.get('HTTP_REFERER'):
		ctx['form_name'] = 'rsvp-focus'
	else:
		ctx['form_name'] = 'rsvp'

	print(ctx['form_name'])

	member = group_handler(request.user)
	ctx['members'] = member.values(person=F("member__full_name"))
	ctx['total_guest'] = member.values('member').count()
	print("total guest: " + str(ctx['total_guest']))
	formset = modelformset_factory(Person, form=RSVPForm, extra=0)

	
	#get a list of values from ctx[members]
	param_dict = list(ctx['members'])
	person_qs = query_values_helper(param_dict)
	print("OLA")
	initial_rsvp = Person.objects.all().filter(full_name__in=person_qs)
	print(initial_rsvp.count())
	form = formset(request.POST or None, queryset=initial_rsvp)
	print("CHIx")
	

	if request.method == 'POST':
		if 'submit' in request.POST:
			for f in form:
				print(f)
			if form.is_valid():
				rsvp = form.save()
				ctx['success'] = 1
				ctx['form_name'] = 'rsvp-focus'
			else:
				print(form.errors)
				ctx['error_focus'] = 'RSVPForm'
				ctx['form_name'] = 'rsvp-focus'
		elif 'back' in request.POST:
			logout(request)
			return redirect('render_rsvp')
	
	ctx['form'] = form

	return render(request, 'snorlax/index_rsvp.html', ctx)

def query_values_helper(param_dict):
	result_dict = {}
	index = 0
	for element in param_dict:
		for key, value in element.items():
			result_dict[index]=value
			index += 1
	values = list(result_dict.values())
	return values



def view_404(request, exception):
    # make a redirect to homepage - in this case, to RSVP page
    # you can use the name of url or just the plain link
    path = '/' + get_language() + '/rsvp'
    return redirect(path)

def view_500(request, template_name='snorlax/500.html'):
	import traceback
	t = loader.get_template(template_name) # You need to create a 500.html template.
	ltype,lvalue,ltraceback = sys.exc_info()
	x = traceback.print_tb(ltraceback)
	ctx = {'type':ltype,'value':lvalue,'traceback':x}
	return http.HttpResponseServerError(t.render(ctx))

