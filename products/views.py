import json
from django.shortcuts import (
    render, get_list_or_404, get_object_or_404
)
from .models import Product


def list_view(request):
    # with open('data.json', 'r') as file:
    #     context = json.load(file)
    # return render(
    #     request,
    #     'products/list.html',
    #     {
    #         'products': context.get('products') or []
    #     }
    # )
    return render(request,'products/list.html',
                  {
                      'products':Product.objects.all()
                  })

def detail_view(request, pk):
    # with open('data.json', 'r') as file:
    #     context = json.load(file)
    #
    # products = context.get('products')
    #
    # return render(
    #     request,
    #     'products/detail.html',
    #     {
    #         'object': products[pk] if len(products) > pk else ''
    #     }
    # )

    return render(request, 'products/detail.html',
                  {
                      'object':  get_object_or_404(Product, id=pk)
                  })
