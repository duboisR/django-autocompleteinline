from django.contrib import admin

import shop.models


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    search_fields = ['name']


class ShopProductInline(admin.TabularInline):
    model = shop.models.ShopProduct
    autocomplete_fields = ['product']
    extra = 1
    verbose_name = 'Produit'
    verbose_name_plural = 'Produits'

    class Media:
        js = ('js/shopproduct_change.js',)


class ShopAdmin(admin.ModelAdmin):
    list_display = ('name', )
    search_fields = ['name']
    inlines = [ShopProductInline]


admin.site.register(shop.models.Product, ProductAdmin)
admin.site.register(shop.models.Shop, ShopAdmin)
