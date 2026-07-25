from django.db import models

class studentModel(models.Model):
    roll=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=30)
    fathers_name=models.CharField(max_length=30)
    address=models.TextField()

    def __str__(self):
        return f'Name: {self.name} - {self.roll}'
    


