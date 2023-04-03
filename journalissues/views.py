from rest_framework.mixins import *
from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from django.core.files.storage import default_storage
from rest_framework.parsers import MultiPartParser
from rest_framework.generics import get_object_or_404

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

class lastIssueView(GenericAPIView, UpdateModelMixin, RetrieveModelMixin, DestroyModelMixin):
    # Override
    def get_queryset(self):
        issues = Issue.objects.all()
        lastissueid = issues[len(issues) - 1].id
        queryset = Issue.objects.filter(pk=lastissueid)
        return queryset
    #Override
    def get_object(self):
        return get_object_or_404(self.get_queryset())
    serializer_class=IssueSerializer
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

class articlesView(GenericAPIView, ListModelMixin, CreateModelMixin):
    serializer_class=ArticleSerializer
    queryset = Article.objects.all()
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    def post(self,request,*args, **kwargs):
        return self.create(request, *args, **kwargs)

class articleView(GenericAPIView, UpdateModelMixin, RetrieveModelMixin, DestroyModelMixin):
    serializer_class=ArticleSerializer
    queryset = Article.objects.all()
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class issueArticlesView(GenericAPIView, ListModelMixin):
    #Override
    def get_queryset(self):
        issue_id = self.kwargs.get('issue_id')
        queryset = Article.objects.filter(issue_id=issue_id)
        return queryset
    serializer_class=ArticleSerializer
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

class lastIssueArticlesView(GenericAPIView, ListModelMixin):
    # Override
    def get_queryset(self):
        issues = Issue.objects.all()
        lastissueid = issues[len(issues) - 1].id
        print(lastissueid)
        queryset = Article.objects.filter(issue_id=lastissueid)
        print(queryset)
        return queryset
    #Override
    def get_object(self):
        return get_object_or_404(self.get_queryset())
    serializer_class=ArticleSerializer
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

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

class SaveIssueFile(APIView):
    parser_classes = (MultiPartParser,) #Oppure: FileUploadParser
    def post(self, request):
        file = request.FILES['file']
        file_name = default_storage.save('issues/' + file.name, file)
        return Response(file_name, status=204)