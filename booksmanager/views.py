from django.shortcuts import render, redirect, HttpResponse
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


def add_author(request):
    if request.method=='POST':
        new_author_name = request.POST.get('author_name')
        books = request.POST.getlist('books')
        new_author = books_models.Author.objects.create(name=new_author_name)
        new_author.book.set(books)
        new_author.save()
        return redirect('/author_list/')
    return render(request, 'add_author.html', {'books': books_models.Book.objects.all()})


def delete_author(request):
    delete_id = request.GET.get('id')
    delete_obj = books_models.Author.objects.get(id=delete_id)
    delete_obj.delete()
    return redirect('/author_list/')


def edit_author(request):
    if request.method == 'POST':
        edit_id = request.POST.get('author_id')
        edit_author_name = request.POST.get('author_name')
        edit_author_books = request.POST.getlist('book_id')
        edit_author_obj = books_models.Author.objects.get(id=edit_id)
        edit_author_obj.name = edit_author_name
        edit_author_obj.book.set(edit_author_books)
        edit_author_obj.save()
        return redirect('/author_list/')

    edit_id = request.GET.get('id')
    edit_author_obj = books_models.Author.objects.get(id=edit_id)
    all_books = books_models.Book.objects.all()
    return render(request, 'edit_author.html', {'author': edit_author_obj, 'books':all_books})


def template_test(request):
    return render(request, 't_test.html')