from django.db import models
from catalog.models import Product

class Order(models.Model):
    STATUS_CHOICES = (
        ('pending', 'В обробці'),
        ('shipping', 'В дорозі'),
        ('completed', 'Виконано'),
        ('cancelled', 'Скасовано'),
    )
    first_name = models.CharField(max_length=100, verbose_name="Ім'я")
    last_name = models.CharField(max_length=100, verbose_name="Прізвище")
    phone = models.CharField(max_length=20, verbose_name="Телефон")
    email = models.EmailField(blank=True, null=True, verbose_name="Email")
    city = models.CharField(max_length=100, verbose_name="Місто")
    address = models.CharField(max_length=250, verbose_name="Адреса / Відділення пошти")
    delivery_method = models.CharField(max_length=50, verbose_name="Спосіб доставки")
    payment_method = models.CharField(max_length=50, verbose_name="Спосіб оплати")
    comment = models.TextField(blank=True, verbose_name="Коментар")
    
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата створення")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending', verbose_name="Статус")
    
    # Якщо користувач залогінений, прив'язуємо замовлення до нього
    user = models.ForeignKey('auth.User', on_delete=models.SET_NULL, null=True, blank=True, related_name='orders', verbose_name="Користувач")

    class Meta:
        verbose_name = "Замовлення"
        verbose_name_plural = "Замовлення"
        ordering = ('-created_at',)
    def __str__(self):
        return f"Замовлення #{self.id} — {self.first_name} {self.last_name}"

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())

    # Допоміжний метод для красивого виведення класів статусів у CSS
    def status_class(self):
        mapping = {
            'pending': 'pending',
            'shipping': 'shipping',
            'completed': 'completed',
            'cancelled': 'cancelled',
        }
        return mapping.get(self.status, 'pending')

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE, verbose_name="Замовлення")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Товар")
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Ціна")
    quantity = models.PositiveIntegerField(default=1, verbose_name="Кількість")

    class Meta:
        verbose_name = "Товар у замовленні"
        verbose_name_plural = "Товари у замовленні"

    def __str__(self):
        return f"{self.product.name} ({self.quantity})"

    def get_cost(self):
        return self.price * self.quantity