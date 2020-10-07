from django.db import models

# Create your models here.
from django.db import models

# 用户模型类
class User(models.Model):
    # 用户账号，要唯一
    userAccount = models.CharField(max_length=20,unique=True)
    # 密码
    userPasswd  = models.CharField(max_length=200)
    # 研究领域
    userField  = models.CharField(max_length=20)
    # 姓名
    userName    =  models.CharField(max_length=20)
    # email
    userEmail   = models.CharField(max_length=50)
    # 隶属组织
    userOrganization = models.CharField(max_length=50)
    # @classmethod
    # def createuser(cls,account,passwd,name,phone,address,img,rank,token):
    #     u = cls(userAccount = account,userPasswd = passwd,userName=name,userPhone=phone,userAdderss=address,userImg=img,userRank=rank,userToken=token)
    #     return u