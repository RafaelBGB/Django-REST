from rest_framework.viewsets import ModelViewSet
from todoapp.models import ToDo, Project
from todoapp.serializers import ToDoModelSerializer, ProjectModelSerializer


class ToDoModelViewSet(ModelViewSet):
    queryset = ToDo.objects.all()
    serializer_class = ToDoModelSerializer


class ProjectModelViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer
