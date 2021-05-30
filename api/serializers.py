from rest_framework import serializers

from .models import *

class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = "__all__"




class CandidateTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestScore
        fields = "__all__"

