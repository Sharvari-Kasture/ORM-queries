from django.urls import path, register_converter
from . import views
from .converters import FloatConverter

# Register the custom converter
register_converter(FloatConverter, 'float')

urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('author/create/', views.create_author, name='create_author'),
    path('book/<int:pk>/', views.book_detail, name='book_detail'),
    path('book/new/', views.book_create, name='book_create'),
    path('book/<int:pk>/edit/', views.book_update, name='book_update'),
    path('book/<int:pk>/delete/', views.book_delete, name='book_delete'),
    path('books/author/<str:author_name>/', views.books_by_author, name='books_by_author'),
    path('books/published_after/<int:year>/', views.books_published_after, name='books_published_after'),
    path('books/price_range/<float:min_price>/<float:max_price>/', views.books_price_range, name='books_price_range'),
    path('books/multiple_criteria/', views.books_multiple_criteria, name='books_multiple_criteria'),
    path('authors_with_book_count/', views.authors_with_book_count, name='authors_with_book_count'),
    path('book_aggregations/', views.book_aggregations, name='book_aggregations'),
    path('books/ordered_by_title/', views.books_ordered_by_title, name='books_ordered_by_title'),
    path('distinct_authors/', views.distinct_authors, name='distinct_authors'),
    path('update_book_prices/', views.update_book_prices, name='update_book_prices'),
    path('raw_sql_query/', views.raw_sql_query, name='raw_sql_query'),
]
