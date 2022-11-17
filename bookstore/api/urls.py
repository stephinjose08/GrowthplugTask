from django.contrib import admin
from django import views

from rest_framework.routers import DefaultRouter




from .views import (UserCreateView,MyTokenObtainPairView,UserListView,BookViewSet,
genreViewSet,ebookCreateView,ebookupdatedeleteView,filterEbokView,genreupdatedeleteView)
from django.urls import path,include
from rest_framework_simplejwt.views import (
  
    TokenRefreshView,TokenObtainPairView
)

router = DefaultRouter()
router.register('book', BookViewSet, basename='book')
router.register('genre', genreViewSet, basename='genre')

urlpatterns = [
    path('',include(router.urls)),
    path('login/', MyTokenObtainPairView.as_view(), name='login-user'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', UserCreateView.as_view(),name='user-create'),
    path('userlist/', UserListView.as_view() ,name='user-list'),
    path('create_book/', ebookCreateView.as_view() ,name='book-create'),
    path('ebookrud/<int:pk>/', ebookupdatedeleteView.as_view() ,name='book-update'),
    path('genrerud/<int:pk>/', genreupdatedeleteView.as_view() ,name='book-update'),

    path('filter/', filterEbokView.as_view() ,name='search'),
]