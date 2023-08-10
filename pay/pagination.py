from rest_framework.pagination import PageNumberPagination


class PayPagination(PageNumberPagination):
    """Класс описания пагинации курсов"""

    page_size = 9  # количество страниц
