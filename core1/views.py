
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializer import *
from .utils import *

DELIVERY = 'Delivery'
PICKUP = 'Pick-up'


class ListBooks(APIView):
    def get(self, request, format=None):
        try:
            book_name = request.GET.get('book')
            if book_name is not None:
                books = Book.objects.filter(name__startswith=book_name)
                if len(books) > 0:
                    serializer = BookSerializer(books, many=True)
                    return Response(serializer.data)
                else:
                    return Response([])
            transaction = request.GET.get('transaction')
            if transaction == DELIVERY or transaction == PICKUP:
                books = Book.objects.filter(
                    transaction=Transaction.objects.get(name=transaction))
                serializer = BookSerializer(books, many=True)
                return Response(serializer.data)
            books = Book.objects.all()
            serializer = BookSerializer(books, many=True)
            return Response(serializer.data)
        except:
            err = ServiceUnavailable()
            return custom_exception_handler(err, "Context")


class ListBookItem(APIView):
    def get(self, request, pk):
        try:
            book = Book.objects.get(id=pk)
            serializer = BookSerializer(book, many=False)
            return Response(serializer.data)
        except:
            err = ServiceUnavailable()
            return custom_exception_handler(err, "Context")


class CategoryList(APIView):
    def get(self, request):
        try:
            category = Category.objects.all()
            serializer = CategorySerializer(category, many=True)
            return Response(serializer.data)
        except:
            err = ServiceUnavailable()
            return custom_exception_handler(err, "Context")


class CategoryItem(APIView):
    def get(self, request, pk):
        try:
            category = Category.objects.get(id=pk)
            serializer = CategorySerializerWithBooks(category, many=False)
            return Response(serializer.data)
        except:
            err = ServiceUnavailable()
            return custom_exception_handler(err, "Context")


class StoreList(APIView):
    def get(self, request):
        deliveryConst = 'Delivery'
        pickupConst = 'Pick-up'
        try:
            transaction = request.GET.get('transaction')
            city = request.GET.get('city')
            if city is not None:
                cityData = City.objects.filter(name__startswith=city)
                if len(cityData) > 0:
                    stores = Store.objects.filter(
                        city=cityData[0])
                    serializer = StoreSerializer(stores, many=True)
                    return Response(serializer.data)
                else:
                    return Response([])
            if transaction == deliveryConst or transaction == pickupConst:
                if transaction == deliveryConst or transaction == pickupConst:
                    storeDelivery = []
                    storePickup = []
                    stores = Store.objects.all()
                    for store in stores:
                        books = store.book_set.all()
                        for book in books:
                            for transactionBook in book.transaction.all():
                                if transactionBook.name == pickupConst:
                                    if store not in storePickup:
                                        storePickup.append(store)
                                else:
                                    if store not in storeDelivery:
                                        storeDelivery.append(store)

                    if transaction == deliveryConst:
                        serializer = StoreSerializer(storeDelivery, many=True)
                        return Response(serializer.data)
                    else:
                        serializer = StoreSerializer(storePickup, many=True)
                        return Response(serializer.data)
                else:
                    err = ServiceUnavailable()
                    return custom_exception_handler(err, "Context")
            else:
                store = Store.objects.all()
                serializer = StoreSerializer(store, many=True)
                return Response(serializer.data)
        except:
            err = ServiceUnavailable()
            return custom_exception_handler(err, "Context")


class StoreItem(APIView):
    def get(self, request, pk):
        try:
            store = Store.objects.get(id=pk)
            print(store)
            serializer = StoreSerializerWithBooks(store, many=False)
            return Response(serializer.data)
        except:
            err = ServiceUnavailable()
            return custom_exception_handler(err, "Context")
