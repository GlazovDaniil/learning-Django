from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Books, Autor, BookInstance, Genre
from django.views import generic

# Create your views here.

def index(request):

    num_books = Books.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    # Доступные книги (статус= 'На складе')
    # Здесь метод 'all()' применен по умолчанию.
    num_instances_availabe = BookInstance.objects.filter(status__exact=2).count()

    # Авторы книг,
    num_authors = Autor.objects.count()

    # Отрисовка НТМL-шаблона index.html с данными
    # внутри переменной context
    return  render(request, 'index.html',
                   context={'num_books': num_books,
                            'num_instances': num_instances,
                            'num_instances_availabe': num_instances_availabe,
                            'num_authors': num_authors,
                            #'num_visits': num_visits
                            },)

class BookListView(generic.ListView):
    model = Books
    paginate_by = 3

class BookDetailView(generic.DetailView):
    model = Books

class AuthorsListView(generic.ListView):
    model = Autor
    paginate_by = 4

def authors(requst):
    return HttpResponse("authors")




    """
    В этих фильтрах использован формат: field_name__match_type, где field_name- имя
    поля, по которому фильтруются данные, а match_type - тип соответствия поля 
    определенному критерию
    
    wild_books = Books.objects.filter(title__contains='дикиe')
    """

