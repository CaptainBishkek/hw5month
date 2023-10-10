from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from . import models
from .models import Category, Product, Review
from .serializers import CategorySerializer, ProductSerializer, ReviewSerializer


@api_view(['GET'])
def category_list(request):
    categories = Category.objects.annotate(products_count=models.Count('product'))
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def category_detail(request, pk):
    try:
        category = Category.objects.get(pk=pk)
    except Category.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = CategorySerializer(category)
    return Response(serializer.data)


@api_view(['GET'])
def product_list(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def product_detail(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = ProductSerializer(product)
    return Response(serializer.data)


@api_view(['GET'])
def review_list(request):
    reviews = Review.objects.all()
    serializer = ReviewSerializer(reviews, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def review_detail(request, pk):
    try:
        review = Review.objects.get(pk=pk)
    except Review.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = ReviewSerializer(review)
    return Response(serializer.data)


@api_view(['GET'])
def product_reviews(request):
    products = Product.objects.all()
    product_data = []
    for product in products:
        serializer = ProductSerializer(product)
        product_data.append(serializer.data)
        reviews = Review.objects.filter(product=product)
        review_serializer = ReviewSerializer(reviews, many=True)
        product_data[-1]['reviews'] = review_serializer.data
    all_reviews = Review.objects.all()
    total_rating = 0
    total_reviews = len(all_reviews)
    for review in all_reviews:
        total_rating += review.rating
    if total_reviews > 0:
        average_rating = total_rating / total_reviews
    else:
        average_rating = 0
    response_data = {
        'products': product_data,
        'average_rating': average_rating
    }
    return Response(response_data)
