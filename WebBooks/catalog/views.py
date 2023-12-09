from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Books, Autor, BookInstance, Genre
from django.views import generic
from django.contrib.auth import logout
from django.shortcuts import redirect

# Create your views here.

def index(request):

    num_books = Books.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    # Доступные книги (статус= 'На складе')
    # Здесь метод 'all()' применен по умолчанию.
    num_instances_availabe = BookInstance.objects.filter(status__exact=2).count()

    # Авторы книг,
    num_authors = Autor.objects.count()

    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    # Отрисовка НТМL-шаблона index.html с данными внутри переменной context
    return  render(request, 'index.html',
                   context={'num_books': num_books,
                            'num_instances': num_instances,
                            'num_instances_availabe': num_instances_availabe,
                            'num_authors': num_authors,
                            'num_visits': num_visits
                            },)

class BookListView(generic.ListView):
    model = Books
    paginate_by = 3

class BookDetailView(generic.DetailView):
    model = Books

class AuthorsListView(generic.ListView):
    model = Autor
    paginate_by = 4

def authors(request):
    return HttpResponse("authors")

def logout_view(request):
    logout(request)
    return redirect('/')

    """
    В этих фильтрах использован формат: field_name__match_type, где field_name- имя
    поля, по которому фильтруются данные, а match_type - тип соответствия поля 
    определенному критерию
    
    wild_books = Books.objects.filter(title__contains='дикиe')
    """

