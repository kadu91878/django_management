from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from models.projects import Project
from serializers.projects_serializer import ProjectSerializer


class ProjectUpdateAPIView(APIView):
    def patch(self, request, pk):
        project = Project.objects.get(pk=pk)
        serializer = ProjectSerializer(project, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
