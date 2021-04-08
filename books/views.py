from django.shortcuts import render

# Create your views here.

from .models import Book
from django.contrib import messages
def Bookshows(request):
    books = Book.objects.all()
    print(books)
    return render(request, "books.html", {'booksdis': books})