from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, \
    UpdateModelMixin
from rest_framework.viewsets import GenericViewSet

from usersapp.models import User
from usersapp.serializers import UsersModelSerializer


class UsersModelViewSet(ListModelMixin, RetrieveModelMixin, UpdateModelMixin,
                        GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UsersModelSerializer
