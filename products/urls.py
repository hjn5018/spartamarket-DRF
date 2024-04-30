from django.urls import path
from . import views


urlpatterns = [
    path('', views.ProductListViewSet.as_view({'get':'list', 'post':'create'})),
    path('<int:product_id>/', views.ProductDetailAPIView.as_view()),
    
]