from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect
from .models import Todo


# Create your views here.
def list_todo_items(request):
    return render(request, 'index.html')


def list_todo_insert(request: HttpRequest):
    todo = Todo(content=request.POST['content'])
    todo.save()
    return redirect('')
