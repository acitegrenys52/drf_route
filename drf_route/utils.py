from rest_framework import viewsets
from rest_framework.request import Request
from rest_framework.response import Response


def get_mixin(obj, request: Request, function: str) -> Response:
    methods = ['list', 'create', 'retrieve', 'update', 'partial_update', 'destroy']
    if function not in methods:
        raise Exception("%s in not in %s" % (function, methods))

    viewset = viewsets.ModelViewSet()
    viewset.get_serializer = obj.get_serializer
    response = getattr(viewset, function)(request)
    return response
