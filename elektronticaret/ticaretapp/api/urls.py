from django.urls import path 
from ticaretapp.api import views

urlpatterns = [
    path('banner/',views.BannerListAPIView.as_view()),
    path('user-create/', views.UserCreateAPIView.as_view()),
    path('product/',views.ProductListAPIView.as_view()),
    path('productcontent/',views.ProductContentListAPIView.as_view()),
    path('productphoto/',views.ProductPhotoListAPIView.as_view()),
    path('review/',views.ReviewListAPIView.as_view()),
    path('sitesettings/',views.SiteSettingsListAPIView.as_view()),
    path('store/',views.StoreListAPIView.as_view()),
    path('wishlist-create/', views.WishlistCreateAPIView.as_view()),
    path('user-wishlist-list/', views.WishlistCreateAPIView.as_view()),
    path('user-basced-list/', views.BascedCreateAPIView.as_view()),
    path('basced-create/', views.BascedCreateAPIView.as_view()),
    path('settings/',views.SiteSettingsListAPIView.as_view()) 

 ]
 