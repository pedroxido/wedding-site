from django.shortcuts import render, redirect

# Create your views here.
def do_rsvp(request):
    return render(request, 'snorlax/index_rsvp.html', {})

def view_404(request):
    # make a redirect to homepage - in this case, to RSVP page
    # you can use the name of url or just the plain link
    return redirect('/rsvp')