from django.http import HttpResponse
from rest_framework import generics
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer


class ProductList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer



"""
# Deprecated in favor of ListAPIView

from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer


class ProductList(APIView):
    def get(self, request, format=None):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
"""
