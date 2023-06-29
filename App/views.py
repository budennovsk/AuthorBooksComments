from django.shortcuts import render, get_object_or_404, redirect
from .models import Author, Books, Comments
from .forms import AppBookForm, CreateCommentForm, UpdateCommentForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required


# Create your views here.
def all(request):
    if request.user.is_anonymous is not True:

        if request.method == "GET":
            # author = Author.objects.all()

            books = Books.objects.filter(actors__user_id=request.user).prefetch_related('actors').all()
            # comments = Comments.objects.select_related('comment_author_id').count()
            context = {
                # 'author': author,
                'books': books,
                'comments': CreateCommentForm
            }
            return render(request, 'app/index.html', context=context)

        if request.method == 'POST':
            form = CreateCommentForm(request.POST)
            form.save()
            return redirect('all')
    else:
        return render(request, 'app/index.html')


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
    if request.method == 'GET':
        print(book_id)
        books = Books.objects.filter(pk=book_id).all()
        print(books)
        forms = AppBookForm()
        return render(request, 'app/book.html', {'books': books, 'forms': forms})

    if request.method == 'POST':
        ls = Books.objects.filter(pk=book_id, actors__user_id=request.user).all()

        for i in ls:
            i.title_name = request.POST['title_name']
            i.Archived = request.POST.get('Archived', False)
            i.save()

        return redirect('all')


def delete(request, book_id_delete):
    if request.method == 'POST':
        books = Books.objects.filter(pk=book_id_delete, actors__user_id=request.user)
        books.delete()
        return redirect('all')


def get_comment(request, comment_id):
    if request.method == "GET":
        comments = Comments.objects.filter(comment_books__id=comment_id, comment_author__user=request.user).all()
        return render(request, 'app/comments.html', {'comments': comments, 'form': UpdateCommentForm()})

    if request.method == 'POST':
        delete_comment = Comments.objects.filter(pk=comment_id, comment_author__user_id=request.user)
        delete_comment.delete()
        return redirect('all')


def update_comments(request, comment_id):
    if request.method == 'POST':
        update = Comments.objects.filter(pk=comment_id, comment_author__user=request.user).all()
        for i in update:
            i.comment = request.POST['comment']
            i.save()
        return redirect('all')


def loginup(request):
    print('ddd')
    if request.method == 'GET':
        return render(request, 'app/login.html', {'form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('all')
            except IntegrityError:
                return render(request, 'app/login.html',
                              {'form': UserCreationForm(), 'error': 'Такой пользователь уже существует'})
        else:

            return render(request, 'app/login.html',
                          {'form': UserCreationForm(), 'error': 'Пароль не совпадает'})


@login_required
def logoutuser(request: object) -> render:
    """ Выход из органайзера"""
    if request.method == 'POST':
        logout(request)
        return redirect('all')


def inlogin(request: object) -> render:
    """ Авторизация пользователя в органайзер """
    if request.method == 'GET':
        return render(request, 'app/inlogin.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'app/inlogin.html',
                          {'form': AuthenticationForm(), 'error': "Пользователь и пароль не существуют"})
        else:
            login(request, user)
            return redirect('all')
