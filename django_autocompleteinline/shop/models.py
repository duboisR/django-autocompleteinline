from django.db import models


class Product(models.Model):
    name = models.CharField(
                verbose_name='Nom',
                max_length=50,
                unique=True)
    price = models.DecimalField(
                verbose_name='Prix',
                max_digits=5,
                decimal_places=2)

    class Meta:
        verbose_name = 'Produit'
        verbose_name_plural = 'Produits'
        ordering = ['name']

    def __str__(self):
        return self.name


class Shop(models.Model):
    name = models.CharField(
                verbose_name='Nom',
                max_length=50,
                unique=True)

    class Meta:
        verbose_name = 'Magasin'
        verbose_name_plural = 'Magasins'
        ordering = ['name']

    def __str__(self):
        return self.name


class ShopProduct(models.Model):
    product = models.ForeignKey(
                'Product',
                verbose_name='Produit',
                on_delete=models.CASCADE)
    shop = models.ForeignKey(
                'Shop',
                verbose_name='Magasin',
                on_delete=models.CASCADE)
    price = models.DecimalField(
                verbose_name='Prix spécifique à ce magasin',
                max_digits=5,
                decimal_places=2)

    class Meta:
        verbose_name = 'Produit du Magasin'
        verbose_name_plural = 'Produits du Magasin'
        unique_together = ('product', 'shop')
        # ordering = ['product']

    def __str__(self):
        return str(self.product)
