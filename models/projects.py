from django.db import models


class Project(models.Model):
    STATUS_CHOICES = [
        ('em andamento', 'Em Andamento'),
        ('concluído', 'Concluído'),
        ('cancelado', 'Cancelado'),
        ('pausado', 'Pausado'),
        ('planejado', 'Planejado'),  # Nova opção adicionada
    ]
    
    
    project_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)
    
    
    

    def __str__(self):
        return self.name
    
    class Meta:
        app_label = 'models'
        db_table = 'projects'
        managed = False
