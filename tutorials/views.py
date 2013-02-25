from django.http import HttpResponseRedirect

def redirect_to_index(request):
    return HttpResponseRedirect('/books/')
