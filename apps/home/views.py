
from rest_framework import viewsets, permissions, renderers
from rest_framework.decorators import action
from rest_framework.response import Response

from home.models import Content, Snippet
from django.contrib.auth.models import User,Group

from rest_framework.viewsets import ModelViewSet,generics

from home.permissions import IsOwnerOrReadOnly
from .serializers import IndexSeriallizer, UserSerializer, GroupSerializer, SnippetSerializer


# Create your views here.

#查询多个
class IndexViewList(generics.ListCreateAPIView):
    queryset =  Content.objects.all()
    serializer_class = IndexSeriallizer

    # def perform_create(self, serializer):
    #     serializer.save(owner=self.request.user)


#查询单个
class IndexDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Content.objects.all()
    serializer_class = IndexSeriallizer
    # def get(self,request):
    #     queryset = Content.objects.all()
    #
    #     serializer = IndexSeriallizer(queryset,many=True)
    #     return Response(serializer.data)
    # # print("serializer_class{}".format(serializer_class.data))


class UserViewSet(viewsets.ModelViewSet):
    """
    允许用户查看或编辑的API路径。
    """

    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    允许组查看或编辑的API路径。
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer



class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class SnippetList(generics.ListCreateAPIView):

    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly)


# class SnippetViewSet(viewsets.ModelViewSet):
#     """
#     此视图自动提供`list`，`create`，`retrieve`，`update`和`destroy`操作。
#
#     另外我们还提供了一个额外的`highlight`操作。
#     """
#     queryset = Snippet.objects.all()
#     serializer_class = SnippetSerializer
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly,
#                           IsOwnerOrReadOnly,)
#
#     @action(renderer_classes=[renderers.StaticHTMLRenderer])
#     def highlight(self, request, *args, **kwargs):
#         snippet = self.get_object()
#         return Response(snippet.highlighted)
#
#     def perform_create(self, serializer):
#         serializer.save(owner=self.request.user)