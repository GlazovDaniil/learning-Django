from django.contrib import admin
from .models import Autor, Books, Genre, Language, Status, BookInstance

# Register your models here.
#admin.site.register(Autor)
#admin.site.register(Books)
admin.site.register(Genre)
admin.site.register(Language)
admin.site.register(Status)
#admin.site.register(BookInstance)

class BooksInstanceInline(admin.TabularInline):
    model = BookInstance

@admin.register(Autor) # используем декоратаор, то же самое что и admin.site.register(Autor)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'last_name', 'date_of_birth', 'date_of_death')
    fields = ['name', 'last_name',
              ('date_of_birth', 'date_of_death')]


@admin.register(Books)
class BooksAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'language', 'display_author')
    list_filter = ('genre', 'autor')
    inlines = [BooksInstanceInline]

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_filter = ('book', 'status')
    fieldsets = (
        ('Экземпляр книги', {'fields': ('book', 'imprint', 'inv_nom')}),
        ('Статус и окончание его действия', {'fields': ('status', 'due_back')}),
    )
