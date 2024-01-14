from django.urls import path
from .views import (
    CreateUserView,
    RetrieveUpdateView,
    )

urlpatterns = [
    path('create/', CreateUserView.as_view()),
    path('profile/', RetrieveUpdateView.as_view()),
]
