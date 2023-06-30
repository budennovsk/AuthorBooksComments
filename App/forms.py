from django.forms import ModelForm
from .models import Book, Comment


class AppBookForm(ModelForm):
    """ Создание формы"""
    class Meta:
        model = Book
        fields = ['title_name', 'Archived']

    def __init__(self, *args, **kwargs):
        """ Изменение формы на стили будстрап"""
        super().__init__(*args, **kwargs)

        for field in iter(self.fields):
            if field == 'title_name':
                self.fields[field].widget.attrs.update({
                    'class': 'form-control'
                })
            else:
                self.fields[field].widget.attrs.update({
                    'class': 'form-check-input',
                    'value': 'True',

                })


class CreateCommentForm(ModelForm):
    """ Создание формы"""
    class Meta:
        model = Comment
        fields = ['comment', 'comment_books', 'comment_author']

    def __init__(self, *args, **kwargs):
        """ Изменение формы на стили будстрап"""
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })


class UpdateCommentForm(ModelForm):
    """ Создание формы"""
    class Meta:
        model = Comment
        fields = ['comment']

    def __init__(self, *args, **kwargs):
        """ Изменение формы на стили будстрап"""
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control',


            })
