from django.db import models

# Create your models here.
class Ad(models.Model):
    game_desc = models.CharField(max_length=50,default="玩游戏领红包")
    game_image_hash=models.CharField(max_length=50,default="05f108ca4e0c543488799f0c7c708cb1jpeg")
    game_is_show = models.BooleanField(default=True)
    game_link = models.CharField(max_length=100,default='https://gamecenter.faas.ele.me')
    gift_mall_desc = models.CharField(max_length=50,default='0元好物在这里')

class Uses(models.Model):
    avatar = models.CharField(max_length=70,verbose_name="头像")
    balance = models.IntegerField(default=0)
    brand_member_new = models.IntegerField(default=0)
    current_address_id = models.IntegerField(default=0)
    current_invoice_id = models.IntegerField(default=0)
    delivery_card_expire_days = models.IntegerField(default=0)
    gift_amount = models.IntegerField(default=3)
    city = models.CharField(max_length=25,verbose_name="城市")
    email = models.EmailField(verbose_name="邮箱")
    registe_time = models.DateTimeField(auto_now=True,verbose_name="注册时间")
    user_id = models.IntegerField(verbose_name="用户id")
    is_active = models.BooleanField(default=1)
    is_email_valid = models.BooleanField(default=False)
    is_mobile_valid = models.BooleanField(default=True)
    mobile = models.CharField(max_length=11)
    point = models.IntegerField()
    username = models.CharField(max_length=20,verbose_name="用户名")
    column_desc = models.ForeignKey("Ad",on_delete=models.CASCADE)

    class Meta:
        app_label = "user"
        db_table = "df_user"
