from django.shortcuts import render
from .models import Author, Publisher

def authors_list(request):
    authors = Author.objects.all()
    return render(request, 'authors_list.html', {'authors': authors})

def publishers_list(request):
    publishers = Publisher.objects.all()
    return render(request, 'publishers_list.html', {'publishers': publishers})


