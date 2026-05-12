from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from game.models import Events
# Create your views here.

def home(request):
    
    #Events.objects.create(title="Python Conf 2026", date="2026-06-12") Создает запись
    events = Events.objects.all() # Возвращает список объектов строк
    #Events.objects.get(id=1) Получить одну строку
    #Events.filter() Выводит строки по условию
    #event.title = "Мастер-класс по Django" Меняет запись
    #event.save() Сохраняет изменения в бд
    #event.delete() удаляет запись
    events1 = [
        {"id": 1, "title": "Python Conf 2026", "date": "2026-06-12", "location": "Moscow"},
        {"id": 2, "title": "Мастер-класс по Django", "date": "2026-05-28", "location": "Nizhny Novgorod"},
        {"id": 3, "title": "Backend Meetup", "date": "2026-07-04", "location": "St-Petersburg"},
    ]
    return render(request, 'form.html', {"events": events})

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