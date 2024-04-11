from rest_framework import serializers

from models.projects import Project


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        # fields = ['project_id', 'name', 'description', 'start_date', 'end_date', 'status']
        fields = '__all__'
        app_label = 'serializers'
