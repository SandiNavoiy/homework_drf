from rest_framework.pagination import PageNumberPagination


class LessonPagination(PageNumberPagination):
    """Класс описания пагинации курсов"""
    page_size = 2  # количество страниц
