from rest_framework.mixins import *
from rest_framework.generics import GenericAPIView
from .models import CallForPapers, Proposal, Proposer, Review
from .serializers import CallForPapersSerializer, ProposalSerializer, ProposerSerializer, ReviewSerializer

class callsForPapersView(GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset = CallForPapers.objects.all()
    serializer_class=CallForPapersSerializer
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    def post(self,request,*args, **kwargs):
        return self.create(request, *args, **kwargs)

class callForPapersView(GenericAPIView, UpdateModelMixin, RetrieveModelMixin, DestroyModelMixin):
    queryset = CallForPapers.objects.all()
    serializer_class=CallForPapersSerializer
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class proposalsView(GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset = Proposal.objects.all()
    serializer_class=ProposalSerializer
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    def post(self,request,*args, **kwargs):
        return self.create(request, *args, **kwargs)

class proposalView(GenericAPIView, UpdateModelMixin, RetrieveModelMixin, DestroyModelMixin):
    queryset = Proposal.objects.all()
    serializer_class=ProposalSerializer
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class proposersView(GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset = Proposer.objects.all()
    serializer_class=ProposerSerializer
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    def post(self,request,*args, **kwargs):
        return self.create(request, *args, **kwargs)

class proposerView(GenericAPIView, UpdateModelMixin, RetrieveModelMixin, DestroyModelMixin):
    queryset = Proposer.objects.all()
    serializer_class=ProposerSerializer
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class reviewsView(GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset = Review.objects.all()
    serializer_class=ReviewSerializer
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    def post(self,request,*args, **kwargs):
        return self.create(request, *args, **kwargs)

class reviewView(GenericAPIView, UpdateModelMixin, RetrieveModelMixin, DestroyModelMixin):
    queryset = Review.objects.all()
    serializer_class=ReviewSerializer
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)