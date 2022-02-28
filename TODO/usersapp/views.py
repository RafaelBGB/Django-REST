from rest_framework.viewsets import ModelViewSet
from usersapp.models import User
from usersapp.serializers import UsersModelSerializer


class UsersModelViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UsersModelSerializer
