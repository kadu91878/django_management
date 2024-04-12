from django.db import models
from models.projects import Project


class Teams(models.Model):
    team_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE, null=True, blank=True, db_column='project_id')
    
    
    class Meta:
        app_label = 'models'
        db_table = 'teams'
        managed = False
   