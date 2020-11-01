from django.db import models
from django.contrib.auth.models import User,Group
# Create your models here.




class MapCity(models.Model):
    title_head = models.CharField(verbose_name="标志",max_length=20000)
    name = models.CharField(verbose_name="类型",max_length=20)
    # _id = models.IntegerField(verbose_name="id")
    id = models.AutoField(verbose_name="id",primary_key=True)
    class Meta:
        app_label = "v1"
        db_table="MapCity"



