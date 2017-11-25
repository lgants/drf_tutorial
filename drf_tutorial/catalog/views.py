from rest_framework import generics, status
from rest_framework.response import Response
from .models import Product, Review
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .serializers import ProductSerializer, ReviewSerializer

# ListCreateAPIView is used for read-write endpoints to represent a collection of model instances
class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAdminOrReadOnly, )
    lookup_url_kwarg = 'product_id'


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAdminOrReadOnly, )
    lookup_url_kwarg = 'product_id'


class ReviewList(generics.ListCreateAPIView):
    serializer_class = ReviewSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )
    lookup_url_kwarg = 'product_id'

    # Need to manually customise the perform_create method because the default one doesn't know to set the created_by and product_id fields
    def perform_create(self, serializer):
        serializer.save(
            created_by=self.request.user,
            product_id=self.kwargs['product_id'])

    def get_queryset(self):
        product = self.kwargs['product_id']
        return Review.objects.filter(product__id=product)


class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ReviewSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)
    lookup_url_kwarg = 'review_id'

    def get_queryset(self):
        review = self.kwargs['review_id']
        return Review.objects.filter(id=review)


"""
# Replaced with ProductDetail(generics.RetrieveUpdateDestroyAPIView):

class ProductDetail(APIView):
    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        product = self.get_object(pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        product = self.get_object(pk)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        product = self.get_object(pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
"""


"""
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Product
from .serializers import ProductSerializer
from rest_framework import status

class ProductList(APIView):
    # Unlike ListAPIView, must explicitly define the GET method
    def get(self, request, format=None):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
"""


"""
from django.http import HttpResponse
from rest_framework import generics
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer

# ListAPIView is used for read-only endpoints to represent a collection of model instances
class ProductList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
"""


"""
# Deprecated in favor of APIView

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
