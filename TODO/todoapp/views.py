from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import LimitOffsetPagination
from django_filters import rest_framework as filters

from todoapp.models import ToDo, Project
from todoapp.serializers import ToDoModelSerializer, ProjectModelSerializer, \
    ToDoModelSerializerBase


class ProjectLimitPagination(LimitOffsetPagination):
    default_limit = 10


class ToDoLimitPagination(LimitOffsetPagination):
    default_limit = 20


class ProjectFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='contains')

    class Meta:
        model = Project
        fields = ['name']


class ToDoFilter(filters.FilterSet):
    create_data = filters.DateTimeFromToRangeFilter(field_name='create_data')

    class Meta:
        model = ToDo
        fields = ['project', 'author', 'status']


class ToDoModelViewSet(ModelViewSet):
    queryset = ToDo.objects.all()
    # serializer_class = ToDoModelSerializer
    pagination_class = ToDoLimitPagination
    filterset_class = ToDoFilter

    def get_serializer_class(self):
        if self.request.method in ['GET']:
            return ToDoModelSerializer
        return ToDoModelSerializerBase


class ProjectModelViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer
    pagination_class = ProjectLimitPagination
    filterset_class = ProjectFilter

