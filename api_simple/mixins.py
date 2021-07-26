from rest_framework.decorators import action
from rest_framework.response import Response
from . import views
from .serializers import PostSerializer


class LikedMixin:

    @action(detail=True, methods=['POST'])
    def like(self, request, pk=None):
        obj = self.get_object()
        views.add_like(obj, request.user)
        return Response()

    @action(detail=True, methods=['POST'])
    def unlike(self, request, pk=None):
        obj = self.get_object()
        views.remove_like(obj, request.user)
        return Response()
