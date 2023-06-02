from django.urls import path
from . import views

urlpatterns = [
    path("", views.index_view, name='index'),
    path("book/", views.BookListView.as_view(), name='list_book'),
    path("book/<int:pk>/detail", views.BookDetailView.as_view(), name='detail_book'),
    path("book/create/", views.BookCreateView.as_view(), name='create_book'),
    path("book/<int:pk>/delete", views.BookDeleteView.as_view(), name="delete_book"),
    path("book/<int:pk>/update", views.BookUpdateView.as_view(), name='update_book'),
]