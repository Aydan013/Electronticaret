from django.shortcuts import render, request

from ticaretapp.models import (
    Banner, Product, ProductContent, ProductPhoto, Review,
    Contact, SiteSettings, Store, Wishlist, Basced
)

def index(requsest):
    banners = Banner.objects.all()
    products = Product.objects.all()
    productcontents = ProductContent.objects.all()
    productphotos = ProductPhoto.objects.all()
    reviews = Review.objects.all()
    contacts = Contact.objects.all()
    sitesettingss = SiteSettings.objects.all()
    stores = Store.objects.all()
    wishlists = Wishlist.objects.all()
    basceds = Basced.objects.all()
    
    context = {
        "banners": banners,
        "products":  products,
        "productcontents": productcontents,
        "productphotos": productphotos,
        "reviews": reviews,
        "contacts": contacts,
        "sitesettingss": sitesettingss,
        "stores": stores,
        "wishlists": wishlists,
        "basceds": basceds,
    }
    return render(request,"index/html",context)

