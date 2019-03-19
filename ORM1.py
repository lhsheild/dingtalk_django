import os


if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dingtalk_django.settings')
    import django
    django.setup()

    from queryfunc import models

    # book = models.Book.objects.all().first()
    # ret = book.publisher.name
    # print(ret)
    #
    # ret = models.Book.objects.filter(id=1).values('publisher__name')
    # print(type(ret), ret)

    # publisher_obj = models.Publisher.objects.all().first()
    # ret = publisher_obj.books.all()
    # for i in ret:
    #     print(i.title)

    # publisher_obj = models.Publisher.objects.all().filter(id=1)
    # ret = publisher_obj.values('books__title')
    # print(ret)

    '''ManyToManyFields'''

    # author_obj = models.Author.objects.filter(id=1)[0]
    # print(author_obj.name)
    # ret = author_obj.books.all()
    # for i in ret:
    #     print(i.title)
    #
    # author_obj.books.create(title='jin自传', publisher_id=3)
    # book_obj = models.Book.objects.filter(id=4)[0]
    # print(book_obj.title)
    # book_objs = models.Book.objects.filter(id__gt=5)
    # author_obj.books.add(*book_objs)

    # book_objs = author_obj.books.filter(id__gt=2)
    # id_l = []
    # for i in book_objs:
    #     id_l.append(i)
    # author_obj.books.set(book_objs)
    #     if i.id < 5:
    #         id_l.append(i.id)
    # author_obj.books.set(id_l)

    # books_obj = models.Book.objects.filter(author=None)
    # print(books_obj)
    # author_obj.books.add(*books_obj)

    from django.db.models import *

    # ret = models.Book.objects.all().aggregate(Avg('price'), Max('price'))
    # print(ret.get('price__avg'))

    # ret = models.Book.objects.all().annotate(author_num=Count('author'))
    # print(ret)
    # for i in ret:
    #     print(i.author_num)

    # ret = models.Author.objects.all().annotate(price_sum=Sum('books__price')).values_list('name', 'price_sum')
    # print(ret)

    models.Book.objects.update(sold=F('sold') * 3)