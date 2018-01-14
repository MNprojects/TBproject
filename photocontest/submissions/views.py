from django.shortcuts import render
from .models import Photo
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm



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



class PhotoListView(generic.ListView):
    model = Photo
    paginate_by = 10

class PhotoDetailView(generic.DetailView):
    model = Photo
    

def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DocumentForm()
    return render(request, 'core/model_form_upload.html', {
        'form': form
    })

@login_required
def home(request):
    return render(request, 'submissions/index.html')

def signup(request):
    return render(request, 'signup.html')
