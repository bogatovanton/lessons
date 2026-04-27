from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return HttpResponse(f"<h1>Hello World</h1>")

def profile(request, eq):
    s_id = 0
    s = ''
    for i in range(len(eq)):
        if eq[i] in '+-*:':
            s_id = i
            s = eq[i]
    
    a = int(eq[:s_id])
    b = int(eq[s_id+1:])

    if (s == '+'):
        return HttpResponse(f"{eq}={a+b}")
    elif (s=='-'):
        return HttpResponse(f"{eq}={a-b}")
    elif (s=='*'):
        return HttpResponse(f"{eq}={a*b}")
    elif (s==':'):
        return HttpResponse(f"{eq}={a / b}")
    else:
        return HttpResponse(f"Некорректный ввод")