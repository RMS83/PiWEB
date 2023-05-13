## Раскомментить если не подключаем фильтры в settings.REST_FRAMEWORK
from django_filters.rest_framework import DjangoFilterBackend
## Раскомментить если не подключаем поиск в settings.REST_FRAMEWORK
from rest_framework.filters import SearchFilter
## Раскомментить если не подключаем сортировку в settings.REST_FRAMEWORK
from rest_framework.filters import OrderingFilter
## Раскомментить если не подключаем пагинацию в settings.REST_FRAMEWORK
#from rest_framework.pagination import LimitOffsetPagination

from rest_framework.viewsets import ModelViewSet

from .models import Product, Stock
from .serializers import ProductSerializer, StockSerializer


class ProductViewSet(ModelViewSet):
    """Продукты:"""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    ## Раскомментить если не подключаем фильтры в settings.REST_FRAMEWORK
    # filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]

    search_fields = ['title', 'description']

    # при необходимости добавьте параметры фильтрации


class StockViewSet(ModelViewSet):
    """Склады:"""
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    # при необходимости добавьте параметры фильтрации

    ## Раскомментить если не подключаем все это в settings.REST_FRAMEWORK
    # filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter] #так или через settings.REST_FRAMEWORK для всех views
    ## Раскомментить если не подключаем пагинацию в settings.REST_FRAMEWORK
    #pagination_class = LimitOffsetPagination


    filterset_fields = ['products']
    ordering_fields = ['positions__quantity', 'positions__price']
