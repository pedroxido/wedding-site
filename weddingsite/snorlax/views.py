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
		print("authenticated :: redirect")
		return redirect('user_login_rsvp')

	ctx = {}
	form = PersonForm(request.POST or None, request.FILES or None)
	ctx['form_name'] = 'person'

	if request.method == 'POST':
		if form.is_valid():
			ctx['person'] = authenticate(name=form.cleaned_data['full_name'])
			login(request, ctx['person'])
			#path = '/' + get_language() + '/rsvp/#rsvp'
			#return http.HttpResponseRedirect(path)
		else:
			ctx['error_focus'] = 'PersonForm'
	
	ctx['form'] = form

	return render(request, 'snorlax/index_rsvp.html', ctx)


@login_required(login_url='/' + get_language() + '/rsvp/#rsvp')
def render_auth_rsvp(request):
	print("calling render_auth_rsvp")
	ctx = {}

	try:
		initial_rsvp = get_object_or_404(RSVP, person=request.user)
		dict_initial_rsvp = model_to_dict(initial_rsvp)
		form = RSVPForm(initial=dict_initial_rsvp)
	except:
		form = RSVPForm(request.POST or None, request.FILES or None)

	ctx['form_name'] = 'rsvp'

	if request.method == 'POST':
		if 'submit' in request.POST:
			if form.is_valid():
				rsvp = form.save(commit=False)
				rsvp.person = request.user
				rsvp.save()
				ctx['success'] = 1
				print("saved RSVP Form")
		elif 'back' in request.POST:
			logout(request)
			return redirect('render_rsvp')
	else:
		ctx['error_focus'] = 'RSVPForm'
	
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