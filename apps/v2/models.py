from django.db import models

# Create your models here.

class Head_content(models.Model):
    id = models.AutoField(primary_key=True,verbose_name="ID")
    is_in_serving=models.BooleanField(verbose_name="显示")
    description = models.CharField(max_length=50,verbose_name="描述")
    title = models.CharField(max_length=20,verbose_name="标题")
    link = models.CharField(max_length=1000,verbose_name="链接")
    image_url = models.CharField(max_length=500,verbose_name="图片链接")
    icon_url = models.CharField(max_length=50,verbose_name="图标",null=True,blank=True)
    title_color = models.CharField(max_length=20,verbose_name="标题颜色",null=True,blank=True)
    class Meta:
        db_table = "head_content"
        app_label = "v2"