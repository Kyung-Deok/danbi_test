from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from config.models import TimeStampModel

from rest_framework.generics import get_object_or_404

# Create your models here.


class Team(TimeStampModel):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, on_delete=models.CASCADE, verbose_name='팀명')

    class Meta:
        verbose_name = 'Teams'

    objects = models.Manager()
    
    def __str__(self):
        return self.name


class User(AbstractBaseUser, TimeStampModel):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50, unique=True, db_column="user_id", varbose_name="유저명")
    password = models.CharField(max_length=50, varbose_name="패스워드")
    team_name = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, varbose_name="소속팀")


    objects = models.Manager()

    USERNAME_FIELD = "username"

    class Meta:
        db_table = "Users"

    def __str__(self):
        return self.username