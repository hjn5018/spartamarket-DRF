from rest_framework.views import APIView
from products.models import Product
from products.serializers import ProductSerializer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


class ProductListAPIView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data)


class ProductDetailAPIView(APIView):
    def get_object(self, product_id):
        return get_object_or_404(Product, id=product_id)

    def put(self, request, product_id):
        product = self.get_object(product_id)
        serializer = ProductSerializer(data=request.data, instance=product)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        
    def delete(self, request, product_id):
        product = self.get_object(product_id)
        product.delete()
        return Response(f"{product_id}번 상품 삭제완료")