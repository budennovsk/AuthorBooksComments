from django.contrib import admin
from .models import Author, Books, Comments


class AuthorAdmin(admin.ModelAdmin):
    list_display = '__all__'


class BookAdmin(admin.ModelAdmin):
    list_display = '__all__'


class CommentsAdmin(admin.ModelAdmin):
    list_display = '__all__'


admin.site.register(Author)
admin.site.register(Books)
admin.site.register(Comments)
# Register your models here.
