from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.db.models import Count, Avg, Max, Min, Sum, Q, F
from .models import Book, Author
from .forms import BookForm, AuthorForm

def create_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('author_list')  # Redirect to the author list page
    else:
        form = AuthorForm()
    return render(request, 'QueriesApp/create_author.html', {'form': form})

# List all books
def book_list(request):
    books = Book.objects.all()
    template = 'QueriesApp/book_list.html'
    context = {'books': books}
    return render(request, template, context )

# View details of a single book
def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    template = 'QueriesApp/book_detail.html'
    context = {'book': book}
    return render(request, template, context )

# Create a new book
def book_create(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    template = 'QueriesApp/book_form.html'
    context = {'form': form}
    return render(request, template, context )

# Update an existing book
def book_update(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_detail', pk=book.pk)
    else:
        form = BookForm(instance=book)
    template = 'QueriesApp/book_form.html'
    context = {'form': form}
    return render(request, template, context )   

# Delete a book
def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        book.delete()
        return redirect('book_list')
    template = 'QueriesApp/book_confirm_delete.html'
    context = {'book': book}
    return render(request, template, context )

# Filter books by author name
def books_by_author(request, author_name):
    books = Book.objects.filter(author__name=author_name)
    template = 'QueriesApp/book_list.html'
    context = {'books': books}
    return render(request, template, context )

# Books published after a certain date
def books_published_after(request, year):
    books = Book.objects.filter(published_date__year__gt=year)
    template = 'QueriesApp/book_list.html'
    context = {'books': books}
    return render(request, template, context )

# Books within a price range
def books_price_range(request, min_price, max_price):
    books = Book.objects.filter(price__range=(min_price, max_price))
    template = 'QueriesApp/book_list.html'
    context = {'books': books}
    return render(request, template, context )

# Books by multiple criteria
def books_multiple_criteria(request):
    books = Book.objects.filter(Q(author__name='John Doe') | Q(published_date__gt='2020-01-01'))
    template = 'QueriesApp/book_list.html'
    context = {'books': books}
    return render(request, template, context )

# List authors with the number of books they have written
def authors_with_book_count(request):
    authors = Author.objects.annotate(book_count=Count('book'))
    template = 'QueriesApp/author_list.html'
    context = {'authors': authors}
    return render(request, template, context )

# Aggregations
def book_aggregations(request):
    average_price = Book.objects.aggregate(Avg('price'))
    max_price = Book.objects.aggregate(Max('price'))
    min_price = Book.objects.aggregate(Min('price'))
    total_price = Book.objects.aggregate(Sum('price'))
    book_count = Book.objects.count()
    template = 'QueriesApp/book_aggregations.html'
    context = {
        'average_price': average_price,
        'max_price': max_price,
        'min_price': min_price,
        'total_price': total_price,
        'book_count': book_count
    }
    return render(request, template, context )

# Order books by title
def books_ordered_by_title(request):
    books = Book.objects.order_by('title')
    template = 'QueriesApp/book_list.html'
    context = {'books': books}
    return render(request, template, context )

# Distinct authors
def distinct_authors(request):
    authors = Author.objects.distinct()
    template = 'QueriesApp/author_list.html'
    context = {'authors': authors}
    return render(request, template, context )

# Using F expressions
def update_book_prices(request):
    Book.objects.update(price=F('price') * 1.1)
    return HttpResponse("Updated book prices by 10%")

# Raw SQL query
def raw_sql_query(request):
    from django.db import connection
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM QueriesApp_book WHERE price > %s", [20])
        rows = cursor.fetchall()
    template = 'QueriesApp/raw_sql_query.html'
    context = {'rows': rows}
    return render(request, template, context )

