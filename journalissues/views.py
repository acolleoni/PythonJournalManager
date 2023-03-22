from rest_framework.mixins import *
from rest_framework.generics import GenericAPIView
from .models import Issue, Article, Author, Category
from .serializers import IssueSerializer, ArticleSerializer, AuthorSerializer, CategorySerializer

class issuesView(GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset = Issue.objects.all()
    serializer_class=IssueSerializer
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    def post(self,request,*args, **kwargs):
        return self.create(request, *args, **kwargs)

class issueView(GenericAPIView, UpdateModelMixin, RetrieveModelMixin, DestroyModelMixin):
    queryset = Issue.objects.all()
    serializer_class=IssueSerializer
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class articlesView(GenericAPIView, ListModelMixin, CreateModelMixin):
    serializer_class=ArticleSerializer
    #Override del metodo get_queryset per ottenere solo gli articoli di un certo numero:
    def get_queryset(self):
        issue_id = self.kwargs.get('issue_id')
        queryset = Article.objects.filter(issue_id=issue_id)
        return queryset
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    def post(self,request,*args, **kwargs):
        return self.create(request, *args, **kwargs)


class articleView(GenericAPIView, UpdateModelMixin, RetrieveModelMixin, DestroyModelMixin):
    serializer_class=ArticleSerializer
    #Override del metodo get_queryset per ottenere solo gli articoli di un certo numero:
    def get_queryset(self):
        issue_id = self.kwargs.get('issue_id')
        queryset = Article.objects.filter(issue_id=issue_id)
        return queryset
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class authorsView(GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset = Author.objects.all()
    serializer_class=AuthorSerializer
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    def post(self,request,*args, **kwargs):
        return self.create(request, *args, **kwargs)

class authorView(GenericAPIView, UpdateModelMixin, RetrieveModelMixin, DestroyModelMixin):
    queryset = Author.objects.all()
    serializer_class=AuthorSerializer
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class categoriesView(GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset = Category.objects.all()
    serializer_class=CategorySerializer
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    def post(self,request,*args, **kwargs):
        return self.create(request, *args, **kwargs)

class categoryView(GenericAPIView, UpdateModelMixin, RetrieveModelMixin, DestroyModelMixin):
    queryset = Category.objects.all()
    serializer_class=CategorySerializer
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)