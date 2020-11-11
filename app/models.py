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
    # 手机号
    userPhone  = models.CharField(max_length=20,default="")
    # 隶属组织
    userOrganization = models.CharField(max_length=50)
    # @classmethod
    # def createuser(cls,account,passwd,name,phone,address,img,rank,token):
    #     u = cls(userAccount = account,userPasswd = passwd,userName=name,userPhone=phone,userAdderss=address,userImg=img,userRank=rank,userToken=token)
    #     return u

class Team(models.Model):
    # 负责人账号，要唯一，负责人是已经注册的用户
    managerAccount =models.CharField(max_length=20,unique=True,default="")
    # 密码
    teamPasswd  = models.CharField(max_length=200)
    # 研究领域
    teamField  = models.CharField(max_length=20,default="")
    # 小组姓名
    teamName    =  models.CharField(max_length=20,default="")
    # 负责人姓名
    managerName    = models.CharField(max_length=20,default="")
    # 负责人email
    managerEmail   = models.CharField(max_length=50,default="")
    # 负责人手机号
    managerPhone  =models.CharField(max_length=20,default="")
    # 负责人隶属组织
    managerOrganization = models.CharField(max_length=50,default="")

class solution_img(models.Model):
    img = models.CharField(max_length=255)

class agri_img(models.Model):
    img = models.CharField(max_length=255)

class simulation_platform_img(models.Model):
    img = models.CharField(max_length=255)

class training_courses_img(models.Model):
    img = models.CharField(max_length=255)

class database_img(models.Model):
    img = models.CharField(max_length=255)

class teammember_img(models.Model):
    img = models.CharField(max_length=255)

class consultant_content_img(models.Model):
    img = models.CharField(max_length=255)

class index_img(models.Model):
    img = models.CharField(max_length=255)

class serviceobject_img(models.Model):
    img = models.CharField(max_length=255)

# produce
class produce_img(models.Model):
    img = models.CharField(max_length=255)






