from django.db import models

# Create your models here.


class APIProject(models.Model):
    name = models.CharField("Project Name", max_length=50, null=False)
    describe = models.TextField("Description", default="")
    status = models.BooleanField("Status", default=1)
    update_time = models.DateTimeField("Time Updated", auto_now=True)
    create_time = models.DateTimeField("Time Created", auto_now_add=True)

    def __str__(self):
        return self.name