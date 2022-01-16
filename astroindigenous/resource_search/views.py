from django.db.models import Q
from django.shortcuts import render

# from .models import Resource

# Create your views here.
def home(request):
    return render(request, "home.html")

def search(request):
    search_text = request.POST.get("searchText", "")
    # TODO: Do actual Search
#     results = Resource.objects.filter(
#         Q(author__contains=search_text) |
#         Q(title__contains=search_text) |
#         Q(summary__contains=search_text)
#     )

    return render(request, "results.html", context={
        'results': [],
        'search_text': search_text
    })
