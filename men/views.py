from rest_framework import generics
from rest_framework.authentication import *
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import *

from .models import Men
from .permissions import IsAdminOrReadOnly
from .serializers import MenSerializer


class Pagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 100


class MenAPIList(generics.ListCreateAPIView):
    queryset = Men.objects.all()
    serializer_class = MenSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    pagination_class = Pagination
    authentication_classes = (TokenAuthentication,)


class MenAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Men.objects.all()
    serializer_class = MenSerializer
    permission_classes = (IsAdminOrReadOnly,)
    authentication_classes = (TokenAuthentication,)


class MenAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Men.objects.all()
    serializer_class = MenSerializer
    permission_classes = (IsAdminOrReadOnly,)
    authentication_classes = (TokenAuthentication,)
