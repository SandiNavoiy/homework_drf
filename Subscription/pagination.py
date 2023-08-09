from rest_framework.pagination import PageNumberPagination


class SubscriptionPagination(PageNumberPagination):
    """Класс описания пагинации курсов"""

    page_size = 20  # количество страниц
