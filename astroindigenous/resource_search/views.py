from django.db.models import Q
from django.shortcuts import render

from resource_search.models import Resource

# Create your views here.
def home(request):
    return render(request, "home.html")

def search(request):
    search_text = request.POST.get("searchText", "")
    pub_format = request.POST.get("contentType", "")

    # results = Resource.objects.filter(
    #     Q(author__icontains=search_text) |
    #     Q(title__icontains=search_text) |
    #     Q(summary__icontains=search_text)
    # )
    search_terms = search_text.split(sep=' ')
    results = Resource.objects.none()
    for term in search_terms:
        results_temp = Resource.objects.filter(Q(author__icontains=term) | Q(title__icontains=term) | Q(summary__icontains=term))
        results = results | results_temp

    if pub_format:
        results = results.filter(formats__name__icontains=pub_format)

    return render(request, "results.html", context={
        'results': results,
        'search_text': search_text
    })
