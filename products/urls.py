from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProductListAPIView.as_view()),
    path('<int:product_id>/', views.ProductDetailAPIView.as_view()),
]
