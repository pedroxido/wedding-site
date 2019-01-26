from django.shortcuts import render, redirect
from django.template import loader
from django.utils.translation import get_language
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import PersonForm, RSVPForm
import sys
from django import http

# Create your views here.
def render_rsvp(request):
	ctx = {}
	form = PersonForm(request.POST or None, request.FILES or None)
	ctx['form_name'] = 'person'
	if request.method == 'POST':
		if form.is_valid():
			print('this is valid')
			ctx['person'] = authenticate(name=form.cleaned_data['full_name'])
			login(request, ctx['person'])
			form = RSVPForm()
			ctx['form_name'] = 'rsvp'
			#path = '/' + get_language() + '/rsvp/#rsvp'
			#return http.HttpResponseRedirect(path)
		else:
			print('this is not valid')
			ctx['error_focus'] = 'PersonForm'
	
	ctx['form'] = form

	return render(request, 'snorlax/index_rsvp.html', ctx)

@login_required(login_url='/' + get_language() + '/rsvp/#rsvp')
def do_rsvp(request):
	print(request.user)
	path = '/' + get_language() + '/rsvp/#rsvp'
	return http.HttpResponseRedirect(path)

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