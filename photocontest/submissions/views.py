from django.shortcuts import render
from .models import Photo

def index(request):
    """
    View function for home page of site.
    """
    # Generate counts of some of the main objects
    numOfPhotos=Photo.objects.all().count()

       
    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'index.html',
        context={'numOfPhotos':numOfPhotos},

    )

from django.views import generic

class PhotoListView(generic.ListView):
    model = Photo
    paginate_by = 10

class PhotoDetailView(generic.DetailView):
    model = Photo
    