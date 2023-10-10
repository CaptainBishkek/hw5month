from rest_framework import serializers

from product.models import Product, Category, Review


class CategorySerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=100, required=True)
    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=150, required=True)
    description = serializers.CharField(max_length=300)
    price = serializers.IntegerField(min_value=1 , required=True)
    category = serializers.IntegerField(required=True)
    class Meta:
        model = Product
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    text = serializers.CharField(max_length=200)
    product = serializers.IntegerField()
    stars = serializers.IntegerField(min_value=1 , max_value=5)
    class Meta:
        model = Review
        fields = '__all__'
