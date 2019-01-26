from django.shortcuts import render, redirect, get_object_or_404
from django.template import loader
from django.utils.translation import get_language
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.forms.models import model_to_dict
from .forms import PersonForm, RSVPForm
from .models import RSVP
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
		if form.is_valid():
			ctx['person'] = authenticate(name=form.cleaned_data['full_name'])
			login(request, ctx['person'])
			return redirect('user_login_rsvp')
		else:
			ctx['error_focus'] = 'PersonForm'
	
	ctx['form'] = form

	return render(request, 'snorlax/index_rsvp.html', ctx)


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

	try:
		initial_rsvp = get_object_or_404(RSVP, person=request.user)
		dict_initial_rsvp = model_to_dict(initial_rsvp)
		form = RSVPForm(request.POST or None,instance=initial_rsvp, initial=dict_initial_rsvp)
	except:
		form = RSVPForm(request.POST or None, request.FILES or None)

	if request.method == 'POST':
		if 'submit' in request.POST:
			if form.is_valid():
				rsvp = form.save(commit=False)
				rsvp.person = request.user
				rsvp.save()
				ctx['success'] = 1
				ctx['form_name'] = 'rsvp-focus'
			else:
				ctx['error_focus'] = 'RSVPForm'
				ctx['form_name'] = 'rsvp-focus'
		elif 'back' in request.POST:
			logout(request)
			return redirect('render_rsvp')
	
	ctx['form'] = form

	return render(request, 'snorlax/index_rsvp.html', ctx)


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