from rest_framework.serializers import HyperlinkedModelSerializer, \
    HyperlinkedRelatedField, ModelSerializer
from usersapp.models import User


class UsersModelSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('uid', 'username', 'first_name', 'last_name',
                  'birthday_year', 'email')


class UserModelSerializerV2(HyperlinkedModelSerializer):
    uid = HyperlinkedRelatedField(read_only=True, view_name='user-detail')

    class Meta:
        model = User
        fields = ('uid', 'username', 'first_name', 'last_name',
                  'birthday_year', 'email', 'is_superuser', 'is_staff')
