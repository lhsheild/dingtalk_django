from django.shortcuts import render
import booksmanager.models as books_models


# Create your views here.
def books_list(request):
    all_books = books_models.Book.objects.all()
    return render(request, 'book_list.html', {'books':all_books})
