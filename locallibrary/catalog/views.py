from django.shortcuts import render
from .models import Author, Book, BookInstance, Genre
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from django.forms import ModelForm, DateInput, ModelMultipleChoiceField, CheckboxSelectMultiple
from django.forms.fields import DateField


def index(request):
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_instances_available = BookInstance.objects.filter(status__exact="Available").count()
    num_authors = Author.objects.all().count()

    return render(request, 'index.html', 
                {
                'num_books': num_books,
                'num_instances': num_instances,
                'num_instances_available': num_instances_available,
                "num_authors": num_authors,
                }
    )


class BooksListView(ListView):
    model = Book
    context_object_name = 'my_book_list'
    template_name = 'books_list.html'


class BookDetailView(DetailView):
    model = Book
    template_name = 'book_detail.html'


class AuthorsListView(ListView):
    model = Author
    context_object_name = 'authors_list'
    template_name = 'authors_list.html'


class AuthorDetailView(DetailView):
    model = Author
    template_name = 'author_detail.html'


class AuthorCreateForm(ModelForm):
    date_of_birth = DateField(required=False, widget=DateInput(attrs={'type': 'date'}))
    date_of_death = DateField(required=False, widget=DateInput(attrs={'type': 'date'}))
    class Meta:
        model = Author
        fields = '__all__'


class AuthorCreateView(CreateView):
    model = Author
    template_name = 'add_author.html'
    form_class = AuthorCreateForm


class BookCreateForm(ModelForm):
    genre = ModelMultipleChoiceField(
        queryset=Genre.objects.all(), widget=CheckboxSelectMultiple()
    )
    class Meta:
        model = Book
        fields = ['title', 'author', 'summary', 'isbn', 'genre', 'language']


class BookCreateView(CreateView):
    model = Book
    template_name = 'add_book.html'
    form_class = BookCreateForm

