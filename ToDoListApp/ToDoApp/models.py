from django.db import models

class ToDo(models.Model):
    pub_date=models.DateTimeField()
    text= models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "ToDo"
