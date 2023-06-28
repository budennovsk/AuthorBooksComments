from django.shortcuts import render, get_object_or_404
from .models import Author, Books, Comments


# Create your views here.
def all(request):
    author = Author.objects.all()
    books = Books.objects.prefetch_related('actors').all()
    # for i in books:
    #     print([f.first_name for f in i.actors.all()])
    comments = Comments.objects.select_related('comment_author_id').count()
    context = {
        'author': author,
        'books': books,
        'comments': comments
    }
    return render(request, 'app/index.html', context=context)


def get_list_books(request, author_id):
    print(author_id)
    # actors = Film.objects.filter(slug=film_slug).prefetch_related('actors')
    # da = Books.objects.filter(id=4).prefetch_related('actors').all()
    # for k in da:
    #     print(k.actors__first_name,'ddd')
    a = Books.objects.filter(actors__id=author_id).all()
    print([i.title_name for i in a])

    fas = Books.objects.filter(pk=author_id).all()
    for i in fas:
        print(i.title_name)
    # list_books = get_object_or_404(Books, pk=author_id)
    return render(request, 'app/list_books.html', {'list_books': a})


def get_book(request, book_id):
    books = Books.objects.filter(pk=book_id).all()
    return render(request, 'app/book.html', {'books': books})
