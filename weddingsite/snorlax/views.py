from django.shortcuts import render, redirect
from django.utils.translation import get_language

# Create your views here.
def do_rsvp(request):
    return render(request, 'snorlax/index_rsvp.html', {})

def view_404(request, exception):
    # make a redirect to homepage - in this case, to RSVP page
    # you can use the name of url or just the plain link
    path = + '/' + get_language() + '/rsvp'
    return redirect(path)