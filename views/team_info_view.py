from django.db import connection
from rest_framework.views import APIView
from rest_framework.response import Response

class TeamInfoAPIView(APIView):
    def get(self, request, team_id):
        with connection.cursor() as cursor:
            cursor.execute(
        """ SELECT u.username, t.name, u.role
                FROM users u
                LEFT JOIN userteams u2 ON u2.user_id = u.user_id
                LEFT JOIN teams t ON u2.team_id = t.team_id
                WHERE t.team_id = %s
        """, [team_id]
            )
            
            results = cursor.fetchall()
            
            return Response(results)
            