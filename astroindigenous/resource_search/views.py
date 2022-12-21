from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from resource_search.models import Resource, Tag

# Create your views here.
def all_tags():
    return Tag.objects.all()
    
def home(request):
    return render(request, "home.html", context={ 'tags': all_tags() })

def search(request):
    search_terms = request.POST.getlist("searchText")
    pub_format = request.POST.get("contentType", "")

    # If the published format is provided, restrict to those
    # resources only
    if pub_format:
        scope = Resource.objects.all()
        scope = scope.filter(formats__name__icontains=pub_format)
    else:
        scope = Resource.objects.all()

    # For each provided search_term, check if it matches one of (OR)
    # our "interesting fields" (the ones we index for searching)
    for search_term in search_terms:
        scope = scope.filter(Q(author__icontains=search_term)  |
                             Q(title__icontains=search_term)   |
                             Q(summary__icontains=search_term) |
                             Q(tags__name=search_term))


    # Render results to template.
    return render(request, "results.html", context={
        'results': scope.distinct(),
        'search_text': ' '.join(search_terms),
        'tags': all_tags()
    })

def details(request, rec_id):
    result = get_object_or_404(Resource, id=rec_id)

    return render(request, "details.html", context={
        'result': result
    })
