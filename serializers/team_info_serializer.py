from rest_framework import serializers


class TeamInfoSerializer(serializers.Serializer):
    username = serializers.CharField()
    team_name = serializers.CharField()
    role = serializers.CharField()