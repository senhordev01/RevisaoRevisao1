from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=100, null= False, blank=False)#titulo
    created_at = models.DateField(auto_now_add=True, null=False, blank=False) #data e hora atual
    deadline = models.DateField(null=False, blank = False) #campo de data
    finished_at = models.DateField(null=True)
                  