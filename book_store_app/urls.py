from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'book', BookViewSet)
router.register(r'author', AuthorViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
