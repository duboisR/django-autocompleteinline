from django.urls import path

import shop.views

urlpatterns = [
    path('api/product_price/', shop.views.product_price),
]
