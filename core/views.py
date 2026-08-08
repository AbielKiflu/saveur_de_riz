from django.shortcuts import render
from .models import MenuItem, GalleryImage, ContactInfo

def home_view(request):
    return render(request, 'core/home.html')

def menu_view(request):
    items = MenuItem.objects.all()
    return render(request, 'core/menu.html', {'items': items})

def gallery_view(request):
    images = GalleryImage.objects.all()
    return render(request, 'core/gallery.html', {'images': images})

def about_view(request):
    return render(request, 'core/about.html')

def contact_view(request):
    contact = ContactInfo.objects.first()
    return render(request, 'core/contact.html', {'contact': contact})