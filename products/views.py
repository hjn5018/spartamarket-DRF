from django.shortcuts import render
from rest_framework.views import APIView

class ProductListAPIView(APIView):
    def get(self, request):
        pass