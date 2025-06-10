from rest_framework.generics import CreateAPIView ,ListAPIView
from ticaretapp.models import CustomUser
from ticaretapp.api.serializers import BannerSerializer, ProductSerializer, ProductContentSerializer, ProductPhotoSerializer, ReviewSerializer, ContactSerializer, StoreSerializer, UserCreateSerializer, WishlistSerializer, BascedSerializer, SiteSettingsSerializer,WishlistCreateSerializer
from ticaretapp.models import Banner, Product, ProductContent, ProductPhoto, Review, Contact, Store,  Wishlist, Basced, SiteSettings, Wishlist, Basced, SiteSettings
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser

class BannerListAPIView(ListAPIView):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer
    
class ProductListAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
class ProductContentListAPIView(ListAPIView):
    queryset = ProductContent.objects.all()
    serializer_class = ProductContentSerializer
    
class ProductPhotoListAPIView(ListAPIView):
    queryset = ProductPhoto.objects.all()
    serializer_class = ProductPhotoSerializer
    
class ReviewListAPIView(ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    
class ContactListAPIView(ListAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    
class StoreListAPIView(ListAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
    
    
class UserCreateAPIView(CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserCreateSerializer
    
class WishlistListAPIView(ListAPIView):
    queryset = Wishlist.objects.all()
    serializer_class = WishlistSerializer
    permission_classes = (IsAdminUser,)
    
class UserWishlistAPIView(ListAPIView):
    def get_queryset(self):
        return Wishlist.objects.filter(
            user =self.request.user
        )
    serializer_class =WishlistSerializer

class WishlistCreateAPIView(CreateAPIView):
    queryset = Wishlist.objects.all()
    serializer_class = WishlistCreateSerializer
    permission_classes=(IsAuthenticated,)
    
    # def create(self, request, *args, **kwargs):
    #      Wishlist.objects.create(
    #         user= request.user,
    #         product = request.data["product"]
             
    #      )
    #      return Response(request.data["product"])
     
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status = status.HTTP_200_OK) # her sey qaydasindadir. 201 yaradilanda olur
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) # sehv olsa.
    
class BascedListAPIView(ListAPIView):
    queryset = Basced.objects.all()
    serializer_class = BascedSerializer
    permission_classes = (IsAdminUser,)
    
    
class UserBascedAPIView(ListAPIView):
    def get_queryset(self):
        return Basced.objects.filter(
            user =self.request.user
        )
    serializer_class =BascedSerializer
    
class BascedCreateAPIView(CreateAPIView):
    queryset = Basced.objects.all()
    serializer_class = BascedSerializer
    permission_classes=(IsAuthenticated,)
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status = status.HTTP_200_OK) # her sey qaydasindadir. 201 yaradilanda olur
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) # sehv olsa.
    
class SiteSettingsListAPIView(ListAPIView):
     queryset = SiteSettings.objects.all()
     serializer_class = SiteSettingsSerializer
    