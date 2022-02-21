from django.db.models import Q
from django.shortcuts import render
from resource_search.models import Resource

# Create your views here.
def home(request):
    return render(request, "home.html")

def search(request):
    search_text = request.POST.get("searchText", "")
    pub_format = request.POST.get("contentType", "")
    
    # ------ original results
    # results = Resource.objects.filter(
    #     Q(author__icontains=search_text) |
    #     Q(title__icontains=search_text) |
    #     Q(summary__icontains=search_text)
    # )
    # ------ search below finds all db entries matching ANY search term
    search_terms = search_text.split(sep=' ')
    # results = Resource.objects.none()
    # for term in search_terms:
    #     results_temp = Resource.objects.filter(Q(author__icontains=term) | Q(title__icontains=term) | Q(summary__icontains=term))
    #     results = results | results_temp
    # ------ search below finds all db entries matching ALL search terms
    allresources = Resource.objects.all()
    results = None
    for term in search_terms:
        if results == None:
            results = allresources.filter(Q(author__icontains=term) | Q(title__icontains=term) | Q(summary__icontains=term))
        else:
            results = results.filter(Q(author__icontains=term) | Q(title__icontains=term) | Q(summary__icontains=term))

    if pub_format:
        results = results.filter(formats__name__icontains=pub_format)
    return render(request, "results.html", context={
        'results': results,
        'search_text': search_text
    })