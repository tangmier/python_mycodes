# from django.http import Http404
# from django.template import TemplateDoesNotExist
# from django.views.generic.base import TemplateView
from django.shortcuts import render_to_response, HttpResponse
from books.models import Book


# Create your views here.
def search(request):
    errors = []
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            errors.append('Enter a search term.')
        elif len(q) > 20:
            errors.append('Please enter at most 20 characters.')
        else:
            books = Book.objects.filter(title__icontains=q)
            return render_to_response('books/search_results.html',
                {'books': books, 'query': q})
    return render_to_response('books/search_form.html',
                                {'errors': errors})
# def search_form(request):
#     return render_to_response('books/search_form.html')
#  def about_pages(request, page):
#     try:
#         return TemplateView.as_view(request, template="about/%s.html" % page)
#     except TemplateDoesNotExist:
#         raise Http404()