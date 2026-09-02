from django.db import models

class Blog(models.Model):

    title = models.CharField(max_length=200)

    content = models.TextField()

    def __str__(self):
        return self.title


# نوشتن Model به تنهایی جدول Database را ایجاد نمی‌کند.
# python manage.py makemigrations
# Django بررسی می‌کند Model ما چه تغییری کرده است و یک Migration می‌سازد.


# Django Migrationها را اجرا می‌کند و تغییرات را روی Database اعمال می‌کند.
# python manage.py migrate


# models.py
#     ↓
# makemigrations
#     ↓
# Migration
#     ↓
# migrate
#     ↓
# Database