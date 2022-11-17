from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework import filters, generics, serializers, status, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView

from bookstore.models import ebook, genreCategory

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


from .serializers import (MyTokenObtainPairSerializer, RegisterSerializer,
                          bookSerializer, genCategorySerializer)


class MyTokenObtainPairView(TokenObtainPairView):
    
         serializer_class = MyTokenObtainPairSerializer





class UserCreateView(APIView):

    def post(self,request):
        username=request.data['username']
        if User.objects.filter(username=username).exists():
            return Response({"detail":"Username already exist try another"},status=status.HTTP_403_FORBIDDEN)
        else:
            serializer=RegisterSerializer(data=request.data)
            if serializer.is_valid():

                    account=serializer.save()
                    
                    refresh = RefreshToken.for_user(account)

                    return Response({
                        'username':account.username,
                    
                        'refresh': str(refresh),
                    'access': str(refresh.access_token),
                    },status=status.HTTP_201_CREATED)
                    
                    #return Response(status=status.HTTP_201_CREATED)
            else:
                return Response(status=status.HTTP_403_FORBIDDEN)


class UserListView(generics.ListAPIView):
    
    queryset = User.objects.all()
    serializer_class =RegisterSerializer
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['username','is_active']

    # filter_backends = [filters.SearchFilter]
    # search_fields = ['username']

class BookViewSet(viewsets.ViewSet):
    
    def list(self, request):
     
        queryset = ebook.objects.all()
        serializer = bookSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        
            queryset = ebook.objects.all()
            book = get_object_or_404(queryset, pk=pk)
            serializer = bookSerializer(book)
            return Response(serializer.data)
 

        
class genreViewSet(viewsets.ViewSet):
    
    def list(self, request):
     
        queryset = genreCategory.objects.all()
        serializer = genCategorySerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        
            queryset = genreCategory.objects.all()
            book = get_object_or_404(queryset, pk=pk)
            serializer = genCategorySerializer(book)
            return Response(serializer.data)
        
class ebookCreateView(APIView):

    def post(self,request):
        serializer=bookSerializer(data=request.data)
        if serializer.is_valid():
           serializer.save()
           return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def put(self,request,pk):

        try:
            book=ebook.objects.get(pk=pk)
            serializer=bookSerializer(book,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        except ebook.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
class ebookupdatedeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset=ebook.objects.all()
    serializer_class=bookSerializer

class genreCreateUpdateDestroyView(APIView):

    def post(self,request):
        serializer=genCategorySerializer(data=request.data)
        if serializer.is_valid():
           serializer.save()
           return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class genreupdatedeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset=genreCategory.objects.all()
    serializer_class=genCategorySerializer

# class searchuser(generics.ListAPIView):
#     queryset=User.objects.all()
#     serializer_class=RegisterSerializer
#     filter_backends = [DjangoFilterBackend]
#     filterset_fields = ['username','is_active']
#     filter_backends = [filters.SearchFilter]
#     search_fields = ['username']

    # def get_queryset(self):
    #      username=self.kwargs['username']
    #      print(username)
    #      return User.objects.filter(username__icontains=username)
class filterEbokView(generics.ListAPIView):
    queryset=ebook.objects.all()
    serializer_class=bookSerializer
    filter_backends = [DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter]
    filterset_fields = ['title','genre__genre']
    search_fields = ['title','genre__genre']
    ordering_fields = ['review','title']