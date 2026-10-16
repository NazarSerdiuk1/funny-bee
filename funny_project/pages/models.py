from django.db import models

class ContactMessage(models.Model):
    name = models.CharField(max_length=100, verbose_name="Ім'я")
    phone = models.CharField(max_length=20, verbose_name="Телефон")
    message = models.TextField(verbose_name="Повідомлення")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата відправки")
    is_processed = models.BooleanField(default=False, verbose_name="Опрацьовано")

    class Meta:
        verbose_name = "Повідомлення з контактів"
        verbose_name_plural = "Повідомлення з контактів"

    def __str__(self):
        return f"{self.name} ({self.phone}) — {self.created_at.strftime('%d.%m.%Y')}"


