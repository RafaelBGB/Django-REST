import graphene
from graphene_django import DjangoObjectType

from todoapp.models import Project, ToDo
from usersapp.models import User


class ProjectType(DjangoObjectType):
    class Meta:
        model = Project
        fields = '__all__'


class ToDoType(DjangoObjectType):
    class Meta:
        model = ToDo
        fields = '__all__'


class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = ('uid', 'username', 'first_name', 'last_name',
                  'birthday_year', 'email',)


class Query(graphene.ObjectType):
    all_projects = graphene.List(ProjectType)
    all_todo = graphene.List(ToDoType)
    project_by_uid = graphene.Field(ProjectType,
                                    uid=graphene.String(required=True))
    todo_by_uid = graphene.Field(ToDoType, uid=graphene.String(required=True))
    all_users = graphene.List(UserType)
    user_by_uid = graphene.Field(UserType, uid=graphene.String(required=True))

    def resolve_all_projects(self, info):
        return Project.objects.all()

    def resolve_all_todo(self, info):
        return ToDo.objects.all()

    def resolve_project_by_uid(self, info, uid):
        try:
            return Project.objects.get(uid=uid)
        except Project.DoesNotExist:
            return None

    def resolve_todo_by_uid(self, info, uid):
        try:
            return ToDo.objects.get(uid=uid)
        except ToDo.DoesNotExist:
            return None

    def resolve_all_users(self, info):
        return User.objects.all()

    def resolve_user_by_uid(self, info, uid):
        try:
            return User.objects.get(uid=uid)
        except User.DoesNotExist:
            return None


class UserInput(graphene.InputObjectType):
    uid = graphene.UUID()


class ToDoCreate(graphene.Mutation):
    class Arguments:
        name_todo = graphene.String(required=True)
        text = graphene.String(required=True)
        project = graphene.UUID(required=True)
        author = graphene.UUID(required=True)
        status = graphene.String()

    todo = graphene.Field(ToDoType)

    @classmethod
    def mutate(cls, root, info, **kwargs):
        todo = ToDo(
            name_todo=kwargs['name_todo'],
            text=kwargs['text']
        )
        try:
            project = Project.objects.get(uid=kwargs['project'])
            author = User.objects.get(uid=kwargs['author'])
            todo.project = project
            todo.author = author
        except Project.DoesNotExist:
            return None
        except User.DoesNotExist:
            return None

        if 'status' in kwargs.keys():
            todo.status = kwargs['status']
        todo.save()
        return ToDoCreate(todo=todo)


class ToDoUpdate(graphene.Mutation):
    class Arguments:
        name_todo = graphene.String()
        text = graphene.String()
        status = graphene.String()
        uid = graphene.UUID()

    todo = graphene.Field(ToDoType)

    @classmethod
    def mutate(cls, root, info, uid, **kwargs):
        todo = ToDo.objects.get(uid=uid)
        if 'name_todo' in kwargs.keys():
            todo.name_todo = kwargs['name_todo']
        if 'text' in kwargs.keys():
            todo.text = kwargs['text']
        if 'status' in kwargs.keys():
            todo.status = kwargs['status']
        todo.save()
        return ToDoUpdate(todo=todo)


class ProjectCreate(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        users = graphene.List(UserInput)
        url_on_repo = graphene.String()

    project = graphene.Field(ProjectType)

    @classmethod
    def mutate(cls, root, info, **kwargs):
        project = Project(name=kwargs['name'])
        if 'url_on_repo' in kwargs.keys():
            project.url_on_repo = kwargs['url_on_repo']
        project.save()
        users = []
        if 'users' in kwargs.keys():
            for val in kwargs['users']:
                try:
                    user = User.objects.get(uid=val.uid)
                    users.append(user)
                except User.DoesNotExist:
                    return None
            project.users.set(users)
        return ProjectCreate(project=project)


class ProjectUpdate(graphene.Mutation):
    class Arguments:
        uid = graphene.UUID()
        name = graphene.String()
        url_on_repo = graphene.String()
        users = graphene.List(UserInput)

    project = graphene.Field(ProjectType)

    @classmethod
    def mutate(cls, root, info, uid, **kwargs):
        project = Project.objects.get(uid=uid)
        users = []
        if 'name' in kwargs.keys():
            project.name = kwargs['name']
        if 'url_on_repo' in kwargs.keys():
            project.url_on_repo = kwargs['url_on_repo']

        project.save()
        if 'users' in kwargs.keys():
            for val in kwargs['users']:
                try:
                    user = User.objects.get(uid=val.uid)
                    users.append(user)
                except User.DoesNotExist:
                    return None
            project.users.set(users)

        return ProjectUpdate(project=project)


class Mutation(graphene.ObjectType):
    create_todo = ToDoCreate.Field()
    update_todo = ToDoUpdate.Field()
    create_project = ProjectCreate.Field()
    update_project = ProjectUpdate.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
