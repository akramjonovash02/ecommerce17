from django.urls import path
from .views import *

urlpatterns = [
    path('categories/', CategoriesAPIView.as_view()),
    path('category/<int:category_id>/details', CategoriesDetailsAPIVIew.as_view()),
    path('sub-categories/', SubCategoriesAPIView.as_view()),
    path('sub-category/<int:subCategory_id>/details', SubCategoriesDetailsAPIVIew.as_view()),
    path('products/', ProductsAPIView.as_view()),
    path('products/<int:product_id>/details', ProductDetailsAPIView.as_view()),

]