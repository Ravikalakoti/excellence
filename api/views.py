from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import CandidateSerializer,CandidateTestSerializer
from .models import *
from rest_framework.response import Response
from rest_framework import status
import pdb

# Create your views here.

def is_user_already_exist(candidate):
 
    candidate_instance = Candidate.objects.filter(id=candidate)
    if not candidate_instance:
        return True, None
    return False, candidate_instance

class CandidateDetail(APIView):
    """
    CandidateDetail
    Created By Ravi Singh
    path: api/candidate/detail
    Api usage: this endpoint used to add the requirement details of candidate.
    """
    def post(self,request):
        """
        request data:
        {
            "candidate_name": "Bhupal Singh",
            "email": "bhu@gmail.com"
           
        }
        response:
            {
                "status": true,
                "candidate_data": {
                    "id": 1,
                    "candidate_name": "Bhupal Singh",
                    "email": "bhu@gmail.com"
                },
                "message": "DONE"
            }
        """
        data = request.data.copy()
        _candidate_serializer = CandidateSerializer(data=data)
        if _candidate_serializer.is_valid():
            _candidate_serializer.save()
        candidate_data = _candidate_serializer.data
        if candidate_data:
            return Response({
                'status': True,
                'candidate_data': candidate_data,
                'message': 'DONE',
            }, status=status.HTTP_200_OK)


    
class CandidateTestScore(APIView):
    """
    CandidateTestScore
    Created By Ravi Singh
    path: api/candidate/score
    Api usage: this endpoint used to add the score of candidate.
    """
    def post(self,request):
        """
        request data:
        {
            "first_round_score": 8,
            "secound_round_score": 7,
            "third_round_score": 6,
            "candidate": 1
        }  
        response:
        {
            "status": true,
            "candidate_data": {
                "id": 2,
                "first_round_score": 8,
                "secound_round_score": 7,
                "third_round_score": 6,
                "candidate": 1
            },
            "message": "DONE"
        }  
        """
        data = request.data.copy()
        candidate_score_serializer = CandidateTestSerializer(data=data)
        if candidate_score_serializer.is_valid():
            candidate_score_serializer.save()
        candidate_score_data = candidate_score_serializer.data
        if candidate_score_data:
            return Response({
                'status': True,
                'candidate_data': candidate_score_data,
                'message': 'DONE',
            }, status=status.HTTP_200_OK) 

        return Response({
                'status': False,
                'message': 'DONE',
            }, status=status.HTTP_204_NO_CONTENT) 


    def get(self,request,candidate):
        candidate_queryset = Candidate.objects.filter(id=candidate).order_by('id')
        if not candidate_queryset:
            return Response({
                'status': False,
                'message': 'DONE',
            }, status=status.HTTP_204_NO_CONTENT)
        candidate_serializer = CandidateTestSerializer(candidate_queryset, many=True) 
        score_data =  candidate_serializer.data
        return Response({
                'status': True,
                'score_data': score_data,
                'message': "done",
            }, status=status.HTTP_200_OK)    








