# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class Location(models.Model):
    id_location = models.IntegerField(primary_key=True)
    country = models.CharField(max_length=20)
    city = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = True #modify
        db_table = 'location'


class Travel(models.Model):
    id_travel = models.IntegerField(primary_key=True)
    target = models.CharField(max_length=100)
    date = models.DateField(blank=True, null=True)
    time = models.TimeField(blank=True, null=True)
    companion = models.CharField(max_length=100)
    location = models.ForeignKey(Location, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = True #modify
        db_table = 'travel'


class PermissionLevel(models.Model):
    class Meta:
        permissions = (
            ('a1', 'can get info'), #(codename, name)
            ('a2', 'can not get info'), #注意結尾要,
        )


from django.contrib.auth.models import User
class VerifyCode(models.Model):
    # 驗證碼
    code = models.CharField(max_length=256)
    # 1對1外鍵,且主鍵被刪除會一起刪掉
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # 資料建立時自動紀錄時間
    c_time = models.DateTimeField(auto_now_add=True)


### advance ###
class City(models.Model):
    # pk讓django定義
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

class Restaurant(models.Model):
    name = models.CharField(max_length=100)    
    star = models.IntegerField(default=5)
    city = models.ForeignKey(City, models.DO_NOTHING, blank=True, null=True)

class Drink(models.Model):
    name = models.CharField(max_length=100)
    suger = models.BooleanField(default=True)
    alcohol = models.BooleanField(default=False)

class Food(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField(default=100)
    quantity = models.IntegerField(default=1)
    drink = models.ForeignKey(Drink, models.DO_NOTHING, blank=True, null=True)
    restaurant = models.ForeignKey(Restaurant, models.DO_NOTHING, blank=True, null=True)