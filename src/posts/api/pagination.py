from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination

class Limitoffsetpagination(LimitOffsetPagination):
    default_limit = 3
    max_limit = 10

class Pagenumberpagination(PageNumberPagination):
    page_size = 4
