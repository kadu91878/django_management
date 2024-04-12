from rest_framework import generics
from models.user_teams import UserTeams
from serializers.user_teams_serializer import UserTeamsSerializer

class UserTeamsListCreateAPIView(generics.ListCreateAPIView):
    queryset = UserTeams.objects.all()
    serializer_class = UserTeamsSerializer


class UserTeamsRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserTeams.objects.all()
    serializer_class = UserTeamsSerializer