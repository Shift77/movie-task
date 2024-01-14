from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, MovieViewSet, RatingViewSet

router = DefaultRouter()
router.register('category', CategoryViewSet)
router.register('movie', MovieViewSet)
router.register('rating', RatingViewSet)

app_name = 'movie'

urlpatterns = [
    path('', include(router.urls))
]
