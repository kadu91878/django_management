from rest_framework import serializers
from models.user_teams import UserTeams


class UserTeamsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserTeams
        fields = '__all__'
        app_label = 'serializers'