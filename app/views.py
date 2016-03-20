from django.contrib.auth.models import User
from rest_framework import mixins, viewsets
from rest_framework.decorators import list_route
from rest_framework.response import Response

from app.serializers import UserSerializer
from drf_route import utils


class UsersViewSet(mixins.RetrieveModelMixin,
                   mixins.ListModelMixin,
                   viewsets.GenericViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    @list_route(methods=['post'])
    def register(self, request) -> Response:
        return utils.get_mixin(self, request, 'create')


UsersViewSet.__doc__ = "Users and everything else"
UsersViewSet.list.__doc__ = 'List of all users'
UsersViewSet.register.__doc__ = "Register new user"
UsersViewSet.retrieve.__doc__ = "Get one user"
