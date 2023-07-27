from django.db import models

# Create your models here.

#方法一：自己定义模型
#缺点：密码需要加密，登陆时候还要密码验证
# class User(models.Model):
#     username = models.CharField(max_length=20,unique = True)
#     password = models.CharField(max_length=20)
#     mobile = models.CharField(max_length=11,unique = True)

#方法二：用django自带模型
from django.contrib.auth.models import AbstractUser
class User(AbstractUser):
    mobile = models.CharField(max_length=11,unique = True)
    
    class Meta:
        db_table ='tb_users'
        verbose_name ='用户管理'
        verbose_name_plural = verbose_name
    