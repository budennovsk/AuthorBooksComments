from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.first_name}-{self.last_name}'


class Books(models.Model):
    title_name = models.CharField(max_length=100)
    Archived = models.BooleanField(default=False)
    actors = models.ManyToManyField(Author)

    def __str__(self):
        return f'{self.title_name}-{self.Archived}-{self.actors}'

class Comments(models.Model):
    comment = models.CharField(max_length=100)
    # comment_books = models.ForeignKey(Books, on_delete=models.CASCADE, null=True)
    comment_author = models.ForeignKey(Author,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return f'{self.comment}-{self.comment_author}'
