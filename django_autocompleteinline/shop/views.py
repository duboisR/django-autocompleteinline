from django.http import JsonResponse

import shop.models


def product_price(request):
    product_name = request.GET.get('product_name', None)
    if product_name:
        product = shop.models.Product.objects.filter(name=product_name).first()
        if product:
            return JsonResponse({'price': product.price})
    return JsonResponse({'price': 0})
