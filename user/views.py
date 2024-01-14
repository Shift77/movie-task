from rest_framework.generics import (
    CreateAPIView,
    RetrieveUpdateAPIView,
    )
from rest_framework.permissions import IsAuthenticated
# from django.contrib.auth import get_user_model
from .serializers import UserSerializer


class CreateUserView(CreateAPIView):
    '''View for creating a user.'''
    serializer_class = UserSerializer


class RetrieveUpdateView(RetrieveUpdateAPIView):
    '''View for retrieving and updating a user.'''
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user
