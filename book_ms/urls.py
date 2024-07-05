from django.urls import path, include
from rest_framework import routers

from book_ms.views import BookViewSet

router = routers.DefaultRouter()  # using router for better practice
router.register("books", BookViewSet)

urlpatterns = [path("", include(router.urls))]

app_name = "book_ms"  # added that variable for correct working urls
