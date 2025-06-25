from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from ticaretapp.models import ( CustomUser,
    Banner, Product, ProductContent, ProductPhoto, Review,
    Contact, SiteSettings, Store, Wishlist, Basced,
)
from django.contrib.admin.sites import AdminSite


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {"fields": ("password",)}),
        (("Personal info"), {"fields": ("first_name", "last_name", "email")}),
        (
            ("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "user_permissions",
                ),
            },
        ),
        (("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "usable_password", "password1", "password2"),
            },
        ),
    )
    list_display = ( "email", "first_name", "last_name", "is_staff")
    search_fields = ( "first_name", "last_name", "email")
    ordering = ("email",)
    readonly_fields = ('date_joined', 'last_login') # deyise bilinmesin deye yaziriq
    
admin.site.register(Banner)
# admin.site.register(Product)
admin.site.register(ProductContent)
admin.site.register(ProductPhoto)
admin.site.register(Review)
admin.site.register(Contact)
admin.site.register(SiteSettings)
admin.site.register(Store)
admin.site.register(Wishlist)
admin.site.register(Basced)

class ProductContentAdmin(admin.TabularInline): # foreginkeyle elaqelendirilmis klaslarda, MANY olan terefi ONE olan terefin icinde gosterir
    model = ProductContent
    extra =1 # admin panelde bos sahelerin sayini gosterir
    
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines =[ProductContentAdmin] # inlines - icinde gostermek istediyimiz klaslari yaziriq
    actions =['make_in_stock','make_not_in_stock']
    
    @admin.action(description="Make selected product in  stock")
    def make_in_stock(self, request, queryset):
        queryset.update(is_stock =True) # trunun yerine istediyimiz qiymetide yaza bilerik
        text = str(len(queryset))+ " product made in stock" if queryset.count() == 1 else str(len(queryset)) + "product made  in stock"
        self.message_user(request, f"{len(queryset)} mehsul silindi.")
        
    @admin.action(description="Make selected product not in  stock")
    def make_not_in_stock(self, request, queryset):
        queryset.update(is_stock =False)
        text = str(len(queryset))+ " product made in stock" if queryset.count() == 1 else str(len(queryset)) + "product made not in stock"
        self.message_user(request,text)
        
    
AdminSite.site_header = "E-commerce Administration"
AdminSite.site_title ="E-commerce"