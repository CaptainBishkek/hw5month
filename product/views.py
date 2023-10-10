from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from .models import Category, Product, Review
from .serializers import CategorySerializer, ProductSerializer, ReviewSerializer


class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ReviewListCreateView(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class ReviewDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class ProductReviewsView(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        products = Product.objects.all()
        for product in products:
            product.reviews = Review.objects.filter(product=product)
        return products

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        total_reviews = Review.objects.count()
        total_rating = sum(review.rating for review in Review.objects.all())
        average_rating = total_rating / total_reviews if total_reviews > 0 else 0

        serializer = self.get_serializer(queryset, many=True)
        data = {
            'products': serializer.data,
            'average_rating': average_rating
        }
        return Response(data)
