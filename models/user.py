from django.db import models

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    role = models.CharField(max_length=50)
    

    def __str__(self):
        return self.username
    
    class Meta:
        app_label = 'models'
        db_table = 'users'
        managed = False
