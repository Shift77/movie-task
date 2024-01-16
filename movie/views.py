from rest_framework import mixins, viewsets
from rest_framework.response import Response
from rest_framework import status
from .serializers import (
    CategorySerializer,
    MovieSerializer,
    RatingSerializer,
    )
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser
    )
from .models import Category, Rating, Movie

class CategoryViewSet(mixins.CreateModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.ListModelMixin,
                      mixins.DestroyModelMixin,
                      viewsets.GenericViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

    def get_permissions(self):
        if self.action == 'retrieve' or self.action == 'list':
            self.permission_classes = [AllowAny]
            return [permission() for permission in self.permission_classes]

        if self.action == 'destroy':
            self.permission_classes = [IsAdminUser]
            return [permission() for permission in self.permission_classes]


        self.permission_classes = [IsAuthenticated]
        return [permission() for permission in self.permission_classes]


class MovieViewSet(viewsets.ModelViewSet):
    '''ViewSet for movie model.'''
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()

    def get_permissions(self):
        if self.action == 'retrieve' or self.action == 'list':
            self.permission_classes = [AllowAny]
            return [permission() for permission in self.permission_classes]

        if self.action == 'destroy':
            self.permission_classes = [IsAdminUser]
            return [permission() for permission in self.permission_classes]

        self.permission_classes = [IsAuthenticated]
        return [permission() for permission in self.permission_classes]

    def update(self, request, *args, **kwargs):
        if self.get_object().user == self.request.user:
            return super().update(request, *args, **kwargs)

        return Response(
            'You dont have authorization to perform such an actions.',
            status=status.HTTP_400_BAD_REQUEST
            )

    def partial_update(self, request, *args, **kwargs):
        if self.get_object().user == self.request.user:
            return super().partial_update(request, *args, **kwargs)

        return Response(
            'You dont have authorization to perform such an actions.',
            status=status.HTTP_400_BAD_REQUEST
            )

    def perform_create(self, serializer):
        '''Setting the author of the movie to the user that performs the action.'''
        return serializer.save(user=self.request.user)


class RatingViewSet(mixins.CreateModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    '''ViewSet to rate movies.'''
    serializer_class = RatingSerializer
    permission_classes = [IsAuthenticated]
    queryset = Rating.objects.all()

    def get_permissions(self):
        if self.action == 'retrieve' or self.action == 'list':
            self.permission_classes = [AllowAny]
            return [permission() for permission in self.permission_classes]

        if self.action == 'destroy':
            self.permission_classes = [IsAdminUser]
            return [permission() for permission in self.permission_classes]

        self.permission_classes = [IsAuthenticated]
        return [permission() for permission in self.permission_classes]

    def update(self, request, *args, **kwargs):
        if self.get_object().user == self.request.user:
            return super().update(request, *args, **kwargs)

        return Response(
            'You dont have authorization to perform such an actions.',
            status=status.HTTP_400_BAD_REQUEST
            )

    def partial_update(self, request, *args, **kwargs):
        if self.get_object().user == self.request.user:
            return super().partial_update(request, *args, **kwargs)

        return Response(
            'You dont have authorization to perform such an actions.',
            status=status.HTTP_400_BAD_REQUEST
            )

    def perform_create(self, serializer):
        '''Setting the author of the movie to the user that performs the action.'''
        return serializer.save(user=self.request.user)
