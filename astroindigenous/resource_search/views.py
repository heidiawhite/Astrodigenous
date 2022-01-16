from django.db.models import Q
from django.shortcuts import render

from resource_search.models import Resource

# Create your views here.
def home(request):
    return render(request, "home.html")

def search(request):
    search_text = request.POST.get("searchText", "")
    # TODO: Do actual Search
    results = Resource.objects.filter(
        Q(author__icontains=search_text) |
        Q(title__icontains=search_text) |
        Q(summary__icontains=search_text)
    )

    return render(request, "results.html", context={
        'results': results,
        'search_text': search_text
    })
