from .models import Product, Review
from rest_framework import serializers


class ReviewSerializer(serializers.ModelSerializer):
    # Serializes user contained in created_by field; returns username instead of the id to make response more human readable
    created_by = serializers.ReadOnlyField(source='created_by.username')

    class Meta:
        model = Review
        fields = ('id', 'title', 'review', 'rating', 'created_by')


class ProductSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'price', 'reviews')
