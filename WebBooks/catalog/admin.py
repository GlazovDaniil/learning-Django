from django.contrib import admin
from .models import Autor, Books, Genre, Language, Status, BookInstance

# Register your models here.
admin.site.register(Autor)
admin.site.register(Books)
admin.site.register(Genre)
admin.site.register(Language)
admin.site.register(Status)
admin.site.register(BookInstance)

