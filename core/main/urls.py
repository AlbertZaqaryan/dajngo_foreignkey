from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeListView.as_view(), name='home'),
    path('<str:id>', views.ProductListView.as_view(), name='product'),
    path('product/<int:id>', views.ProductDetailView.as_view(), name='product_detail')

]