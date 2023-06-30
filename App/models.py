from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')

    def __str__(self):
        return f'{self.first_name}-{self.last_name}-{self.user}'


class Book(models.Model):
    title_name = models.CharField(max_length=100)
    Archived = models.BooleanField(default=True)
    actors = models.ManyToManyField(Author)

    def __str__(self):
        return f'{self.title_name}-{self.Archived}-{self.actors}'


class Comment(models.Model):
    comment = models.CharField(max_length=100)
    comment_books = models.ForeignKey(Book, on_delete=models.CASCADE, null=True)
    comment_author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.comment}-{self.comment_author}'

