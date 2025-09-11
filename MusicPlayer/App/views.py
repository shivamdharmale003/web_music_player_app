from django.shortcuts import render
from .models import Song
from django.core.paginator import Paginator

def index(request):
    songs = Song.objects.all().order_by('id')  # Ordering added
    paginator = Paginator(songs, 1)  # Show 1 song per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {"page_obj": page_obj}
    return render(request, "index.html", context)
