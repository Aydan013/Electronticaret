from rest_framework import serializers
from ticaretapp.models import Banner, Product, ProductContent, ProductPhoto, Review, Contact, SiteSettings, Store,  Wishlist, Basced, SiteSettings
from ticaretapp.models import CustomUser
from django.contrib.auth.password_validation import validate_password #passvordumuzu tesdiqleyen kod. smalik falan natmaq olmur ve s

class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = "__all__"
        
class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only= True)
    class Meta:
        model = CustomUser
        fields = ("username", "password")
        
    def validate(self, data):
        validate_password(data ["password"])
        return data
    
        
    def create(self, validated_data):
        username = validated_data["username"] 
        password = validated_data["password"]
        
        user = CustomUser.objects.create_user(
            username = username,
            password=password  # sadece create edende yazilir

        )
        return user 
      
        # user.set_password(password)
        # user.save()
      # hem create hemde update edende yazilir

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
        
class ProductContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductContent
        fileds = "__all__"

class ProductPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductPhoto
        fields = "__all__"
        
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"
        
class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model =Contact
        fields = "__all__"
        
class SiteSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteSettings
        fields = "__all__"
        
class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = "__all__"
        

class WishlistSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    class Meta:
        model = Wishlist
        fields = "__all__"
        
class WishlistCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wishlist
        fields = ("product",)

class BascedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Basced
        fields = "__all__"

class BascedCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wishlist
        fields = ("product",)
        
class SiteSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model= SiteSettings
        fields = "__all__"

