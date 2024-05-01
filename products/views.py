from rest_framework.views import APIView
from products.models import Product
from products.serializers import ProductSerializer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework import status, pagination
from rest_framework.viewsets import ModelViewSet


class ProductPagination(pagination.CursorPagination):
    page_size = 4
    ordering = "-created_at"
    cursor_query_param = "cursor"

    def get_paginated_response(self, data):
        if self.get_previous_link() is None:
            return Response(
                {
                    "meta": {"code": 301, "message": "OK"},
                    "data": {
                        "next": self.get_next_link(),
                        "previous": self.get_previous_link(),
                        "products": data,
                    },
                },
                status=status.HTTP_301_MOVED_PERMANENTLY,
            )
        else:
            return Response(
                {
                    "meta": {"code": 200, "message": "OK"},
                    "data": {
                        "next": self.get_next_link(),
                        "previous": self.get_previous_link(),
                        "products": data,
                    },
                },
                status=status.HTTP_200_OK,
            )
        

class ProductListViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = ProductPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class ProductDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, product_id):
        return get_object_or_404(Product, id=product_id)

    def put(self, request, product_id):
        product = self.get_object(product_id)
        if request.user == product.author:
            serializer = ProductSerializer(data=request.data, instance=product)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
        else:
            return Response("권한이 없습니다.", status=status.HTTP_403_FORBIDDEN)
        
    def delete(self, request, product_id):
        product = self.get_object(product_id)
        if request.user == product.author:
            product.delete()
            return Response(f"{product_id}번 상품 삭제완료")
        else:
            return Response("권한이 없습니다.", status=status.HTTP_403_FORBIDDEN)