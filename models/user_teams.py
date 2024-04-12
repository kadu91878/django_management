from django.db import models

from models.teams import Teams
from models.user import User


class UserTeams(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, db_column='team_id', primary_key=True)
    team_id = models.ForeignKey(Teams, on_delete=models.CASCADE, db_column='user_id', primary_key=True)

    class Meta:
        db_table = 'userteams'
        app_label = 'models'
        managed = False
        
       
   
