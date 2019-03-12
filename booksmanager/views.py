from django.shortcuts import render, redirect
import booksmanager.models as books_models


# Create your views here.
def books_list(request):
    all_books = books_models.Book.objects.all()
    return render(request, 'book_list.html', {'books': all_books})


def add_book(request):
    if request.method == 'GET':
        all_publishers = books_models.Publisher.objects.all()
        return render(request, 'add_book.html', {'publishers': all_publishers}, {'error': None})
    elif request.method == 'POST':
        try:
            book_title = request.POST.get('book_title')
            publisher_id = request.POST.get('publisher_id')
            books_models.Book.objects.create(title=book_title, publisher_id=publisher_id)
            return redirect('/books_list/')
        except Exception:
            return render('add_book.html', {'publishers': books_models.Publisher.objects.all()}, {'error': '添加失败'})


def delete_book(request):
    if request.method == 'GET':
        delete_id = request.GET.get('id')
        delete_obj = books_models.Book.objects.get(id=delete_id)
        delete_obj.delete()
        return redirect('/books_list/')


def edit_book(request):
    if request.method == 'GET':
        book_id = request.GET.get('id')
        all_books = books_models.Book.objects.all()
        edit_book = all_books.get(id=book_id)
        all_publishers = books_models.Publisher.objects.all()
        return render(request, 'edit_book.html', {'book': edit_book, 'publisher_list': all_publishers})
    elif request.method == 'POST':
        edit_id = request.POST.get('id')
        new_title = request.POST.get('book_title')
        new_publisher_id = request.POST.get('publisher_id')
        edit_obj = books_models.Book.objects.get(id=edit_id)
        edit_obj.title = new_title
        edit_obj.publisher_id = new_publisher_id
        edit_obj.save()
        return redirect('/books_list/')


def author_list(request):
    all_author = books_models.Author.objects.all()
    return render(request, 'author_list.html', {'author_list': all_author})
