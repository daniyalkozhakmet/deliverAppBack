
from unicodedata import category
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializer import *
from .utils import *

class ListBooks(APIView):
    def get(self, request, format=None):
        books=Book.objects.all()
        serializer=BookSerializer(books,many=True)
        return Response(serializer.data)
class ListBookItem(APIView):
    def get(self,request,pk):
        try:
            book=Book.objects.get(id=pk)
            serializer=BookSerializer(book,many=False)
            return Response(serializer.data)
        except:
            err=ServiceUnavailable()
            return custom_exception_handler(err,"Context")
class CategoryList(APIView):
    def get(self,request):
        try:
            category=Category.objects.all()
            serializer=CategorySerializer(category,many=True)
            return Response(serializer.data)
        except:
            err=ServiceUnavailable()
            return custom_exception_handler(err,"Context")
class CategoryItem(APIView):
    def get(self,request,pk):
        try:
            category=Category.objects.get(id=pk)
            serializer=CategorySerializerWithBooks(category,many=False)
            return Response(serializer.data)
        except:
            err=ServiceUnavailable()
            return custom_exception_handler(err,"Context")
class StoreList(APIView):
    def get(self,request):
        try:
            store=Store.objects.all()
            serializer=StoreSerializer(store,many=True)
            return Response(serializer.data)
        except:
            err=ServiceUnavailable()
            return custom_exception_handler(err,"Context")
class StoreItem(APIView):
    def get(self,request,pk):
        try:
            store=Store.objects.get(id=pk)
            serializer=StoreSerializerWithBooks(store,many=False)
            return Response(serializer.data)
        except:
            err=ServiceUnavailable()
            return custom_exception_handler(err,"Context")

