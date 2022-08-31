from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Category, Product
# Create your views here.

class HomeListView(ListView):
    template_name = 'home.html'

    def get(self, request):
        category = Category.objects.all()
        return render(request, self.template_name, {'category':category})

class ProductListView(ListView):
    template_name = 'home_detail.html'

    def get(self, request, id):
        product = Category.objects.filter(pk=id)
        return render(request, self.template_name, {'product':product})


class ProductDetailView(DetailView):

    template_name = 'home_detail_detail.html'

    def get(self, request, id):
        prod = Product.objects.get(pk=id)
        return render(request, self.template_name, {'prod':prod})
