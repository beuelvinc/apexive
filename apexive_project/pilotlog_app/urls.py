from django.urls import re_path, include
from rest_framework.routers import DefaultRouter
from .views import BaseModelViewSet

# Create a router instance
router = DefaultRouter()

# Register the viewset with a default basename
router.register(r'', BaseModelViewSet, basename='base')

urlpatterns = [
    # Use re_path to capture dynamic table_name and route to the viewset
    re_path(r'^(?P<table_name>[\w-]+)/', include(router.urls)),
]
