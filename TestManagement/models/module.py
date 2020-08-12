from django.db import models
from TestManagement.models.project import APIProject

# Create your models here.


class APIModule(models.Model):
    project = models.ForeignKey(APIProject, on_delete=models.CASCADE)
    name = models.CharField("Module Name", max_length=50, null=False)
    describe = models.TextField("Description", default="")
    create_time = models.DateTimeField("Time Created", auto_now_add=True)

    def __str__(self):
        return self.name