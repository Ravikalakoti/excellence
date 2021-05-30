from django.urls import path

from .views import CandidateDetail,CandidateTestScore



urlpatterns = [
    path('detail',CandidateDetail.as_view(),name='candidate_details'),
    path('score',CandidateTestScore.as_view(),name='candidate_score'),
    path('score/<int:candidate>',CandidateTestScore.as_view(),name='candidate_score'),
]