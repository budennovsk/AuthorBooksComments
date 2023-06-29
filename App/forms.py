from django.forms import ModelForm
from .models import Books, Comments


class AppBookForm(ModelForm):
    class Meta:
        model = Books
        fields = ['title_name', 'Archived']

    def __init__(self, *args, **kwargs):
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
    class Meta:
        model = Comments
        fields = ['comment', 'comment_books', 'comment_author']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })


class UpdateCommentForm(ModelForm):
    class Meta:
        model = Comments
        fields = ['comment']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
