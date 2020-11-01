from django.db import models

# Create your models here.

KIN=(
    ("python","python"),
    ("javascript","javascript")
)
class Moment(models.Model):
    create_time = models.DateTimeField(max_length=20)
    content = models.CharField(max_length=20)
    user_name = models.CharField(max_length=202)
    kin = models.CharField(max_length=20,choices=KIN,default=KIN[0])
    class Meta:
        db_table = "index_Moment"
        app_label = "index"









