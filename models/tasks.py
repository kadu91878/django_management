from django.db import models
from models.user import User
from models.projects import Project


STATUS_CHOICES = [
        ('em andamento', 'Em Andamento'),
        ('concluído', 'Concluído'),
        ('cancelado', 'Cancelado'),
        ('pausado', 'Pausado'),
        ('planejado', 'Planejado'),  # Nova opção adicionada
    ]

class Tasks(models.Model):
    task_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)
    start_date = models.DateField(null=True, blank=True)
    due_date = models.DateField(null=True, blank=True)
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, db_column='assigned_to')
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE, null=True, blank=True, db_column='project_id')
    
    
    class Meta:
        app_label = 'models'
        db_table = 'tasks'
        managed = False
        