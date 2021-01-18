from django.shortcuts import render, HttpResponse
from .models import ToDo, Books


def homepage(request):
    return render(request, "index.html")


def test(request):
    todo_list = ToDo.objects.all() 
    return render(request, "test.html", {"todo_list": todo_list})


def second(request):
    return HttpResponse("test 2 page")

def test2(request):
    books_store = Books.objects.all() 
    return render(request, "books.html", {"book_store": books_store})

