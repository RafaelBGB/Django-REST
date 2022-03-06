from rest_framework.serializers import HyperlinkedModelSerializer, \
    HyperlinkedRelatedField
from usersapp.models import User


class UsersModelSerializer(HyperlinkedModelSerializer):
    uid = HyperlinkedRelatedField(
        read_only=True,
        view_name='user-detail'
    )

    class Meta:
        model = User
        fields = ('uid', 'username', 'first_name', 'last_name',
                  'birthday_year', 'email')



