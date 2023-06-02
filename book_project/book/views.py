from django.views.generic import CreateView, ListView, DetailView, DeleteView, UpdateView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import BookModel

# Create your views here.

def index_view(request):
    book_obj_list = BookModel.objects.all().order_by('category')
    return render(request, 'book/index.html', {'book_obj_list':book_obj_list})


class BookListView(ListView):
    template_name = 'book/book_list.html'
    model = BookModel
    
    
class BookDetailView(DetailView):
    template_name = "book/book_detail.html"
    model = BookModel
    
    
class BookCreateView(CreateView):
    template_name = "book/book_create.html"
    model = BookModel
    fields = ('title', 'author', 'category')
    success_url = reverse_lazy('list_book')


class BookDeleteView(DeleteView):
    template_name = "book/book_delete.html"
    model = BookModel
    success_url = reverse_lazy('list_book')
    
class BookUpdateView(UpdateView):
    template_name = "book/book_update.html"
    queryset = BookModel.objects.all()
    fields = ('title', 'author', 'category', 'evaluation', 'finished_date', 'reports')
    success_url = reverse_lazy('list_book')