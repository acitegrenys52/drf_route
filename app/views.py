from django.contrib.auth.models import User
from rest_framework import mixins, viewsets
from rest_framework.decorators import list_route
from rest_framework.response import Response

from app.serializers import UserSerializer
from drf_route import utils


class UsersViewSet(mixins.RetrieveModelMixin,
                   mixins.ListModelMixin,
                   viewsets.GenericViewSet):
    """Users and everything else"""
    serializer_class = UserSerializer
    queryset = User.objects.all()

    @list_route(methods=['post'])
    def register(self, request) -> Response:
        """Register new user"""
        return utils.get_mixin(self, request, 'create')
    register.__doc__ = "lol"


UsersViewSet.list.__doc__ = 'List of all users'
UsersViewSet.retrieve.__doc__ = "Get one user"

print('test')