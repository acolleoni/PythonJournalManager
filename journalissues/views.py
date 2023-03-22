from rest_framework.mixins import *
from rest_framework.generics import GenericAPIView
from .models import Issue
from .serializers import IssueSerializer

class issuesView(GenericAPIView, ListModelMixin, CreateModelMixin, UpdateModelMixin):
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
