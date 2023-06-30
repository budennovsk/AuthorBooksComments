from django.shortcuts import render, get_object_or_404, redirect, get_list_or_404
from .models import Author, Book, Comment
from .forms import AppBookForm, CreateCommentForm, UpdateCommentForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required



def all(request: object) -> render:
    """ Функция отображения рабочей страницы"""
    if request.user.is_anonymous is not True:
        if request.method == "GET":
            books = Book.objects.filter(actors__user_id=request.user).prefetch_related('actors').all()
            context = {
                'books': books,
                'comments': CreateCommentForm
            }
            return render(request, 'app/index.html', context=context)
        elif request.method == 'POST':
            form = CreateCommentForm(request.POST)
            form.save()
            return redirect('all')
    else:
        return render(request, 'app/index.html')


def get_list_books(request: object, author_id: int) -> render:
    """ Функция отображения списка книг автора"""
    list_books = get_list_or_404(Book, actors__id=author_id)
    return render(request, 'app/list_books.html', {'list_books': list_books})

@login_required
def get_book(request: object, book_id: int) -> render:
    """ Функция отображения книги автора"""
    if request.method == 'GET':
        books = get_list_or_404(Book, pk=book_id)
        forms = AppBookForm()
        return render(request, 'app/book.html', {'books': books, 'forms': forms})
    if request.method == 'POST':
        update_books = get_list_or_404(Book, pk=book_id, actors__user_id=request.user)
        for items in update_books:
            items.title_name = request.POST['title_name']
            items.Archived = request.POST.get('Archived', False)
            items.save()
        return redirect('all')

@login_required
def delete(request: object, book_id_delete: int) -> render:
    """ Функция удаления книги автора"""
    delete_book = get_object_or_404(Book, pk=book_id_delete, actors__user_id=request.user)
    if request.method == 'POST':
        delete_book.delete()
        return redirect('all')

@login_required
def get_comment(request: object, comment_id: int) -> render:
    """ Функция отображения списка комментариев автора"""
    if request.method == "GET":
        comments = get_list_or_404(Comment, comment_books__id=comment_id, comment_author__user=request.user)
        return render(request, 'app/comments.html', {'comments': comments, 'form': UpdateCommentForm()})
    if request.method == 'POST':
        delete_comment = get_object_or_404(Comment, pk=comment_id, comment_author__user_id=request.user)
        delete_comment.delete()
        return redirect('all')

@login_required
def update_comments(request: object, comment_id: int) -> render:
    """ Функция изменения комментариев автора"""
    if request.method == 'POST':
        update_com = get_list_or_404(Comment, pk=comment_id, comment_author__user=request.user)
        for items in update_com:
            items.comment = request.POST['comment']
            items.save()
        return redirect('all')


def loginup(request: object) -> render:
    """ Функция регистрации автора"""
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
    """ Выход из профиля"""
    if request.method == 'POST':
        logout(request)
        return redirect('all')


def inlogin(request: object) -> render:
    """ Авторизация пользователя """
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
