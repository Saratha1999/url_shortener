from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Shortened_URL

# Create your views here.

def shorten_url(request):
    if request.method == "POST":
        original_url = request.POST.get("original_url") # Get the original URL from the form submission

        # Check if URL already exists in the database
        obj, created = Shortened_URL.objects.get_or_create(original_url = original_url)

        # Render the result page with the short code if the URL exists or was created
        return render (request, "shortener/result.html", {"original_url": original_url, "short_code": obj.short_code})
    
    return render(request, "shortener/home.html") # If GET request, render the home page

def redirect_url(request, short_code):
    obj = get_object_or_404(Shortened_URL, short_code = short_code)  # Fetch the URL object using the short code

    return redirect (obj.original_url) # Redirect the user to the original URL




