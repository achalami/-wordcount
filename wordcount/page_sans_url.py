from django.http import HttpResponse

def fonction0(request):
    return HttpResponse("""cette page est afiicher par default
    si aucun url nest taper+fonction0""")

def fonction1(request):
    return HttpResponse(""" ce message est different du premier
     et est afiicher par default si aucun url nest taper+fonction1""")
