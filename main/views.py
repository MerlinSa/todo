from django.shortcuts import render, HttpResponse, redirect
from .models import ToDo
from .models import ToMeet
from .models import Habits

# Create your views here.
def homepage(request):
    return render(request, "index.html")

def test(request):
    todo_list = ToDo.objects.all()
    return render(request, 'test.html', {"todo_list": todo_list})

def test2(request):
    tomeet_list = ToMeet.objects.all()
    return render(request, 'meeting.html', {"tomeet_list": tomeet_list})

def add_todo(request):
    form = request.POST
    text = form["todo_text"]
    todo = ToDo(text=text)
    todo.save()
    return redirect(test)

def delete_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.delete()
    return redirect(test)

def mark_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.is_favorite = True
    todo.save()
    return redirect(test)
 
def unmark_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.is_favorite = False
    todo.save()
    return redirect(test)

def close_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.is_closed = not todo.is_closed
    todo.save()
    return redirect(test)

def add_tomeet(request): #дз
    form = request.POST
    text = form["tomeet_text"]
    tomeet = ToMeet(text=text)
    tomeet.save()
    return redirect(test2)

def delete_tomeet(request, id): #Создайте функцию delete_to_meet для модели ToMeet и подключите ее к кнопке удалить.
    tomeet = ToMeet.objects.get(id=id)
    tomeet.delete()
    return redirect(test2)

def mark_tomeet(request, id):  #Создайте функцию mark_to_meet для модели ToMeet. (урок 31) Подключите ее к подходящей кнопке.
    tomeet = ToMeet.objects.get(id=id)
    tomeet.is_favorite = True
    tomeet.save()
    return redirect(test2) 
    
def unmark_tomeet(request, id):  #Создайте функцию unmark_to_meet для модели ToMeet.
    tomeet = ToMeet.objects.get(id=id)
    tomeet.is_favorite = False
    tomeet.save()
    return redirect(test2)  

def close_tomeet(request, id):
    tomeet = ToMeet.objects.get(id=id)
    tomeet.is_closed = not tomeet.is_closed
    tomeet.save()
    return redirect(test2)


def habit1(request):
    habits_list = Habits.objects.all()
    return render(request, 'habits.html', {"habits_list": habits_list})

def add_habits(request):
    form = request.POST
    text = form["habits_text"]
    habits = Habits(text=text)
    habits.save()
    return redirect(habit1)






# def second(request):
#     return HttpResponse("test 2 page")
    