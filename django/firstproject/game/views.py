from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import JsonResponse
from game.models import Events
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
# Create your views here.

def home(request):
    
    #Events.objects.create(title="Python Conf 2026", date="2026-06-12") Создает запись
    events = Events.objects.all() # Возвращает список объектов строк
    #Events.objects.get(id=1) Получить одну строку
    #Events.filter() Выводит строки по условию
    #event.title = "Мастер-класс по Django" Меняет запись
    #event.save() Сохраняет изменения в бд
    #event.delete() удаляет запись
    # events1 = [
    #     {"id": 1, "title": "Python Conf 2026", "date": "2026-06-12", "location": "Moscow"},
    #     {"id": 2, "title": "Мастер-класс по Django", "date": "2026-05-28", "location": "Nizhny Novgorod"},
    #     {"id": 3, "title": "Backend Meetup", "date": "2026-07-04", "location": "St-Petersburg"},
    # ]
    # return render(request, 'form.html', {"events": events})
    user = request.user
    first_name = user.first_name
    return render(request, 'form.html', {'name': first_name, 'events': events})

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
    
def registration(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_login')
    else:
        form = UserCreationForm()
    
    return render(request, 'register.html', {'form': form.as_p})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    
    return render(request, 'registration/login.html', {'form': form})
