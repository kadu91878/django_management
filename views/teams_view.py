from rest_framework import generics

from models.teams import Teams
from serializers.teams_serializer import TeamSerializer


class TeamsListCreateAPIView(generics.ListCreateAPIView):
    queryset = Teams.objects.all()
    serializer_class = TeamSerializer


class TeamsRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Teams.objects.all()
    serializer_class = Teams