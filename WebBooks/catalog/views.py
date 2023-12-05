from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Books
# Create your views here.

def index(request):
    a_record = Books(name="Книгa о вкусной еде")

    """
    В этихфильтрах использован формат: field_name__match_type, где field_name- имя
    поля, по которому фильтруются данные, а match_type - тип соответствия поля 
    определенному критерию
    
    wild_books = Books.objects.filter(title__contains='дикиe')
    """

    a_record.save()
    return HttpResponse("Main page WebBook!")