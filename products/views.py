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

# =====================Pagination적용 전의 ProductList=============================
# class ProductListAPIView(APIView):
#     def get_permissions(self):
#         if self.request.method == 'GET':
#             self.permission_classes = []
#         else:
#             self.permission_classes = [IsAuthenticated, ]
#         return [permission() for permission in self.permission_classes]

#     def get(self, request):
#         products = Product.objects.all()
#         serializer = ProductSerializer(products, many=True)
#         return Response(serializer.data)
    
#     def post(self, request):
#         serializer = ProductSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#         return Response(serializer.data)
# ==========================================================

class ProductDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]

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