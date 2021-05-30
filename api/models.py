from django.db import models

# Create your models here.


class Candidate(models.Model):
    candidate_name = models.CharField(max_length=250,null=True,blank=True)
    email = models.EmailField(null=True,blank=True)

    def __str__(self):
        return str(self.candidate_name)

class TestScore(models.Model):
    candidate_name = models.ForeignKey(Candidate,on_delete=models.CASCADE,null=True,blank=True,)
    first_round_score = models.PositiveIntegerField(null=True,blank=True)
    secound_round_score = models.PositiveIntegerField(null=True,blank=True)
    third_round_score = models.PositiveIntegerField(null=True,blank=True)

    def __str__(self):
        return str(self.candidate_name)

