from django.shortcuts import render
from .models import Photo
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from .forms import SignUpForm
from django.contrib.auth import login, authenticate
from .forms import PhotoForm




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

    def get_queryset(self):
        filter_val = self.request.GET.get('filter', '2018-01-14')
        order = self.request.GET.get('orderby', 'dateTaken')
        new_context = Photo.objects.filter(
            dateTaken=filter_val,
        ).order_by(order)
        return new_context

    def get_context_data(self, **kwargs):
        context = super(PhotoListView, self).get_context_data(**kwargs)
        context['filter'] = self.request.GET.get('filter', '2018-01-01')
        context['orderby'] = self.request.GET.get('orderby', 'dateTaken')
        return context

class PhotoDetailView(generic.DetailView):
    model = Photo
    

def model_form_upload(request):
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('photos')
    else:
        form = PhotoForm()
    return render(request, 'submissions/model_form_upload.html', {
        'form': form
    })

@login_required
def home(request):
    return render(request, 'submissions/index.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('photos')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})
