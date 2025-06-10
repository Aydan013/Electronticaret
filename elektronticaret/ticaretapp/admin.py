from django.contrib import admin

from ticaretapp.models import (
    Banner, Product, ProductContent, ProductPhoto, Review,
    Contact, SiteSettings, Store, Wishlist, Basced,
)

admin.site.register(Banner)
admin.site.register(Product)
admin.site.register(ProductContent)
admin.site.register(ProductPhoto)
admin.site.register(Review)
admin.site.register(Contact)
admin.site.register(SiteSettings)
admin.site.register(Store)
admin.site.register(Wishlist)
admin.site.register(Basced)