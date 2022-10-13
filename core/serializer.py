from .models import *
from rest_framework import serializers
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields='__all__'
class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model=City
        fields='__all__'
class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Transaction
        fields='__all__'
class BookSerializer(serializers.ModelSerializer):
    category=serializers.SerializerMethodField(read_only=True)
    transaction=serializers.SerializerMethodField(read_only=True)
    store=serializers.SerializerMethodField(read_only=True)
    class Meta:
        model=Book
        # depth=1
        fields=['id','name','image','transaction','store','category']
    def get_category(self,obj):
        serializer=CategorySerializer(obj.category,many=True)
        return serializer.data
    def get_transaction(self,obj):
        serializer=TransactionSerializer(obj.transaction.all(),many=True)
        return serializer.data
    def get_store(self,obj):
        serializer=StoreSerializer(obj.store,many=False)
        return serializer.data
class StoreSerializer(serializers.ModelSerializer):
    city=serializers.SerializerMethodField(read_only=True)
    class Meta:
        model=Store
        fields='__all__'
    def get_city(self,obj):
        print(obj.city)
        serializer=CitySerializer(obj.city,many=False)
        return serializer.data
# For category
class BookSerializerWithoutCategory(serializers.ModelSerializer):
    transaction=serializers.SerializerMethodField(read_only=True)
    store=serializers.SerializerMethodField(read_only=True)
    class Meta:
        model=Book
        # depth=1
        fields=['id','name','image','transaction','store',]
    def get_transaction(self,obj):
        serializer=TransactionSerializer(obj.transaction.all(),many=True)
        return serializer.data
    def get_store(self,obj):
        serializer=StoreSerializer(obj.store,many=False)
        return serializer.data    
class CategorySerializerWithBooks(serializers.ModelSerializer):
    books=serializers.SerializerMethodField(read_only=True)
    class Meta:
        model=Category
        # depth=1
        fields=['id','name','books']
    def get_books(self,obj):
        serilizer=BookSerializerWithoutCategory(obj.book_set.all(),many=True)
        return serilizer.data
# For Category
class BookSerializerWithoutStore(serializers.ModelSerializer):
    category=serializers.SerializerMethodField(read_only=True)
    transaction=serializers.SerializerMethodField(read_only=True)
    class Meta:
        model=Book
        # depth=1
        fields=['id','name','image','transaction','category']
    def get_category(self,obj):
        serializer=CategorySerializer(obj.category,many=True)
        return serializer.data
    def get_transaction(self,obj):
        serializer=TransactionSerializer(obj.transaction.all(),many=True)
        return serializer.data
class StoreSerializerWithBooks(serializers.ModelSerializer):
    books=serializers.SerializerMethodField(read_only=True)
    city=serializers.SerializerMethodField(read_only=True)
    class Meta:
        model=Category
        depth=1
        fields=['id','name','books','rating','review','city']
    def get_books(self,obj):
        books=Book.objects.filter(store=obj.id)
        serilizer=BookSerializerWithoutStore(books,many=True)
        return serilizer.data
    def get_city(self,obj):
        print(obj.city)
        serializer=CitySerializer(obj.city,many=False)
        return serializer.data