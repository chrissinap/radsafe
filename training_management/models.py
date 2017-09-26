import datetime

from django.db import models
from django.utils import timezone


class Profile(models.Model):
    name = models.CharField('姓名',max_length=32)

    GENDER_CHOICES = (
        ('M', '男'),
        ('F', '女'),
    )
    gender = models.CharField(
        '性别',
        max_length=1,
        choices=GENDER_CHOICES
    )

    identification_number = models.CharField('身份证号', max_length=18)     # 需判断填报是否准确
    phone_number = models.CharField('手机号码', max_length=11)   # 需判断填报是否准确

    DEPARTMENT_CHOICES = (
        ('KYC', '科研管理处'),
        ('KYTJ', '科研条件处'),
        ('RJC', '人事教育处'),
    )
    department = models.CharField(
        '部门',
        max_length=4,
        choices=DEPARTMENT_CHOICES,
    )

    SECTOR_CHOICES = (
        ('GL', '管理片'),
        ('GY', '光源片'),
        ('HN', '核能片'),
    )
    sector = models.CharField(
        '所属片区',
        max_length=2,
        choices=SECTOR_CHOICES,
    )

    VALIDATION_CHOICES = (
        ('ZG', '在岗'),
        ('LZ', '离职'),
        ('BY', '毕业'),
        ('LG', '调离岗位'),
    )

    is_valid = models.CharField(
        '在岗情况',
        max_length=2,
        choices=VALIDATION_CHOICES,
        default='ZG',
    )

    def __str__(self):
        return self.name


class Certification(models.Model):
    user_profile = models.ForeignKey(Profile)
    TYPE_CHOICES = (
        ('SH', '上海市级'),
        ('GC', '国家初级'),
        ('GZ', '国家中级'),
    )
    training_type = models.CharField(
        '培训类型',
        max_length=2,
        choices=TYPE_CHOICES,
    )

    training_organization = models.CharField('培训机构', max_length=20)

    date_training = models.DateTimeField('培训日期')
    date_expired = models.DateTimeField('有效期至')
    certification_number = models.CharField('证书编号', max_length=20)

    def __str__(self):
        return self.training_type








