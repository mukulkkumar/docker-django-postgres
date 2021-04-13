from rest_framework.viewsets import ModelViewSet
from .serializers import *
from .models import *

# Create your views here.


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
