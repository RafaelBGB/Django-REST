from rest_framework.serializers import HyperlinkedModelSerializer
from usersapp.models import User


class UsersModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = User
        # fields = '__all__'
        fields = ('uid', 'username', 'first_name', 'last_name', 'email')
