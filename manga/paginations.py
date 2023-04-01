from rest_framework.pagination import PageNumberPagination


class MangaPagination(PageNumberPagination):
    page_size = 12
    max_page_size = 200
    page_query_param = "page"


class GenrePagination(PageNumberPagination):
    page_size = 5
    max_page_size = 30
    page_query_param = "page"
