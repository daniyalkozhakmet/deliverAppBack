from django.urls import path,include
from core import views
urlpatterns = [
    path('book/',views.ListBooks.as_view()),
    path('book/<str:pk>',views.ListBookItem.as_view()),
    path('category/',views.CategoryList.as_view()),
    path('category/<str:pk>',views.CategoryItem.as_view()),
    path('store/',views.StoreList.as_view()),
    path('store/<str:pk>',views.StoreItem.as_view()),
]
