from django.contrib import admin
from pay.models import Pay

@admin.register(Pay)
class PayAdmin(admin.ModelAdmin):
    list_display = ('pay_date', 'pay_sum', 'payment_type')  # отображение на дисплее
    list_filter = ('pay_date', 'pay_sum', 'payment_type')  # фильтр
    search_fields = ('pay_date', 'pay_sum', 'payment_type')  # поля поиска

