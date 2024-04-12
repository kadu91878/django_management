from rest_framework import serializers
from models.tasks import Tasks


class TasksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = '__all__'
        app_label = 'serializers'