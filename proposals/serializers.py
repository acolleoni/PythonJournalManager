from rest_framework import serializers
from .models import CallForPapers, Proposal, Proposer, Review

class CallForPapersSerializer(serializers.ModelSerializer):
    class Meta:
        model=CallForPapers
        fields='__all__'

class ProposalSerializer(serializers.ModelSerializer):
    class Meta:
        model=Proposal
        fields='__all__'

class ProposerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Proposer
        fields='__all__'

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model=Review
        fields='__all__'