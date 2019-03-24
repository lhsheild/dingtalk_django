from django.shortcuts import render
from orm import models


# Create your views here.
def books(request):
    from utils.mypage import Page
    p = request.GET.get('page')
    books = models.Book.objects.all()

    total_count = books.count()
    my_page = Page(p, total_count, 'books', per_page=20, max_page=10)
    my_data_start = my_page.data_start
    my_data_end = my_page.data_end
    my_page_html = my_page.page_html()

    current_page_books = books[my_data_start:my_data_end]

    return render(request, 'books.html', {'books': current_page_books, 'total_page': my_page_html})


    # # 获取用户选择页数
    # p = request.GET.get('page')
    #
    # # 所有书籍对象
    # book_objs = models.Book.objects.all()
    # total = book_objs.count()
    # print('total:', total)
    #
    # # 每页的数量
    # per_page = 10
    #
    # # 分页的页数
    # total_page, m = divmod(total, per_page)
    # if m:
    #     total_page += 1
    # try:
    #     p = int(p)
    #     if p > total_page:
    #         p = total_page
    # except Exception as e:
    #     p = 1
    #
    # # 当前页面的数据在数据库的取值范围
    # data_start = (p - 1) * 10
    # data_end = p * 10
    # max_page = 11  # 页面同时展示的最大页码数
    #
    # if total_page < max_page:
    #     max_page = total_page
    #
    # half_max_page = max_page // 2
    #
    # page_start = p - half_max_page
    # page_end = p + half_max_page
    # if page_start <= 1:
    #     page_start = 1
    #     page_end = max_page
    # if page_end >= total_page:
    #     page_end = total_page
    #     page_start = total_page-max_page+1
    #
    # current_page_books = models.Book.objects.all()[data_start:data_end]
    # for i in current_page_books:
    #     print(i.title)
    #
    # html_str_list = []  # 后台拼接前端页码控件
    # html_str_list.append('<li><a href="/books/?page=1">首页</a></li>')
    # if p <= 1:
    #     html_str_list.append('<li class="disabled"><a href="#" aria-label="Previous"><span '
    #                          'aria-hidden="true">&laquo;</span></a></li>')
    # else:
    #     html_str_list.append('<li><a href="/books/?page={}" aria-label="Previous"><span '
    #                          'aria-hidden="true">&laquo;</span></a></li>'.format(p - 1))
    # for i in range(page_start, page_end + 1):
    #     if i == p:
    #         tmp = '<li class="active"><a href="/books/?page={}">{}</a></li>'.format(i, i)
    #     else:
    #         tmp = '<li><a href="/books/?page={}">{}</a></li>'.format(i, i)
    #     html_str_list.append(tmp)
    #
    # if p >= total_page:
    #     html_str_list.append('<li class="disabled"><a href="#" aria-label="Previous"><span '
    #                          'aria-hidden="true">&raquo;</span></a></li>')
    # else:
    #     html_str_list.append('<li><a href="/books/?page={}" aria-label="Previous"><span '
    #                          'aria-hidden="true">&raquo;</span></a></li>'.format(p + 1))
    # html_str_list.append('<li><a href="/books/?page={}">尾页</a></li>'.format(total_page))
    #
    # return render(request, 'books.html', {'books': current_page_books, 'total_page': html_str_list})
