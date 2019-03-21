from django.shortcuts import render
from orm import models


# Create your views here.
def books(request, p):
    p = int(p)
    start = (p - 1) * 10
    end = p * 10

    total = models.Book.objects.all().count()
    total_page, m = divmod(total, 10)
    if m:
        total_page += 1

    all_book = models.Book.objects.all()[start:end]
    html_str_list = []
    for i in range(1,total_page+1):
        tmp = '<li><a href="/books/{}">{}</a></li>'.format(i,i)
        html_str_list.append(tmp)
    return render(request, 'books.html', {'books': all_book, 'total_page':html_str_list})
