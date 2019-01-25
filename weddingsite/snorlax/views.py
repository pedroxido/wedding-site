from django.shortcuts import render, redirect
from django.template import loader
from django.utils.translation import get_language
import sys
from django import http

# Create your views here.
def do_rsvp(request):
    return render(request, 'snorlax/index_rsvp.html', {})

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