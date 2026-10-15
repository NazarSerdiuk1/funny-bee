from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Назва категорії")
    slug = models.SlugField(unique=True, verbose_name="URL (slug)")

    class Meta:
        verbose_name = "Категорія"
        verbose_name_plural = "Категорії"

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', verbose_name="Категорія")
    name = models.CharField(max_length=200, verbose_name="Назва товару")
    slug = models.SlugField(unique=True, verbose_name="URL (slug)")
    description = models.TextField(blank=True, verbose_name="Опис")
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Ціна (грн)")
    image = models.ImageField(upload_to='products/', blank=True, null=True, verbose_name="Зображення")
    is_hit = models.BooleanField(default=False, verbose_name="Хіт продажу")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата створення")

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товари"

    def __str__(self):
        return self.name