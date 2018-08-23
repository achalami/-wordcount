
from django.http import HttpResponse
from django.shortcuts import render

def fonction3(request):
    return HttpResponse("ceci est page afficher a avec url3 +fonction3")

def fonction4(request):
    return HttpResponse("ceci est page afficher a avec url4 + fonction4 ")

def fonctionhttp(request):
    return HttpResponse("""<h1>TEST HTTP OU HTML: pour ne pas ecrire un grand
    code html dans une fonction,
     on le met dans une template ou forme </h1>""")


def homepage(request):

     return render(request,'home.html',{'kle':'ici avec la KLE du dictionaire: voir la fonction home page'})


def count(request):
     notre_variable=request.GET['notre_variable']
     #print(notre_variable)# regarde le resultat dans le terminal
     list_notre_variable=notre_variable.split()
     count=len(list_notre_variable)


     return render(request,'count.html',{'notre_variable':notre_variable,"list_notre_variable":list_notre_variable,'count':count})


def about(request):

     return render(request,'about.html')
