from rest_framework.serializers import HyperlinkedModelSerializer, \
    StringRelatedField, ChoiceField, ModelSerializer

from todoapp.models import ToDo, Project


class ProjectModelSerializer(HyperlinkedModelSerializer):
    users = StringRelatedField(many=True)

    class Meta:
        model = Project
        fields = '__all__'


class ToDoModelSerializer(ModelSerializer):
    author = StringRelatedField()
    status = ChoiceField(ToDo.STATUS_CHOICES)

    class Meta:
        model = ToDo
        fields = '__all__'


class ToDoModelSerializerBase(ModelSerializer):
    class Meta:
        model = ToDo
        fields = '__all__'
