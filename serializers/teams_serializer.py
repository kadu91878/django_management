from rest_framework import serializers
from models.teams import Teams


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teams
        fields = '__all__'
        app_label = 'serializers'