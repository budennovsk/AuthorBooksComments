from django.contrib import admin
from .models import Author, Book, Comment



class AuthorAdmin(admin.ModelAdmin):
    list_display = '__all__'



class BookAdmin(admin.ModelAdmin):
    list_display = '__all__'


class CommentsAdmin(admin.ModelAdmin):
    list_display = '__all__'


admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Comment)
# Register your models here.
