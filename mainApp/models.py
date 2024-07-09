from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=100)
    icon = models.ImageField(upload_to='category_icons', blank=True)

    def __str__(self):
        return self.title

class SubCategory(models.Model):
    title = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} ({self.category.title})"

class Product(models.Model):
    name = models.CharField(max_length=255)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    expiration_date = models.DateField(blank=True, null=True)
    discount = models.IntegerField(default=0)
    amount = models.IntegerField(default=0)
    country = models.CharField(max_length=50, blank=True)
    ordered = models.IntegerField(default=0)
    rated = models.BooleanField(default=False)
    rating = models.PositiveSmallIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    brand = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name

class Image(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
#    path = models.?
    main = models.BooleanField
