from django.db import models

class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=[
        ('Starters', 'Starters'),
        ('Mains', 'Signature Mains'),
        ('Desserts', 'Desserts & Drinks')
    ])
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='menu_images/', blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.category})"


class GalleryImage(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='gallery_images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class ContactInfo(models.Model):
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    facebook_link = models.URLField(blank=True, null=True)
    zalo_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return "Catering Contact Details"