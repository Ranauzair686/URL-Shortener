from django.shortcuts import render, get_object_or_404, redirect
from .models import URL
from .forms import URLForm

def index(request):
    form = URLForm(request.POST or None)
    short_url = None

    if form.is_valid():
        long_url = form.cleaned_data['long_url']
        obj, created = URL.objects.get_or_create(long_url=long_url)
        short_url = request.build_absolute_uri('/') + obj.short_url

    return render(request, 'shortener/index.html', {'form': form, 'short_url': short_url})

def redirect_to_long_url(request, short_url):
    url = get_object_or_404(URL, short_url=short_url)
    return redirect(url.long_url)
