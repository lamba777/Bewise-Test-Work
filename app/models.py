from django.db import models

class Quiz(models.Model):
    id = models.IntegerField(primary_key=True)
    question = models.CharField(max_length=1500)
    answer = models.CharField(max_length=250)
    created_at = models.DateTimeField()
    time_update = models.DateTimeField(auto_now=True)
    previous_question = models.CharField(max_length=1500, null=True)
    
    def __str__(self):
        return str(self.answer)