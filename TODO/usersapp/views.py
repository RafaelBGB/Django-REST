from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, \
    UpdateModelMixin
from rest_framework.viewsets import GenericViewSet

from usersapp.models import User
from usersapp.serializers import UsersModelSerializer, UserModelSerializerV2


class UsersModelViewSet(ListModelMixin, RetrieveModelMixin, UpdateModelMixin,
                        GenericViewSet):
    queryset = User.objects.all()
    # serializer_class = UsersModelSerializer

    def get_serializer_class(self):
        if self.request.version == '2':
            return UserModelSerializerV2
        return UsersModelSerializer
