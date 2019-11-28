from datetime import datetime

from django.db import models

# Create your models here.
class User(models.Model):
    #属性
    # id = models.AutoField() # 自增
    # id = models.IntegerField(primary_key=True) # 需要设置primary_key=True
    username = models.CharField(max_length=15) #设置最大长度为15
    password = models.CharField(max_length=12)
    age = models.IntegerField() # int类型字段
    sex = models.BooleanField(default=False) # bool类型字段
    phone = models.CharField(max_length=11)
    # join_date = models.DateTimeField(default=datetime.now) # 也是显示时间的字段，需要导入from datetime import datetime
    join_date = models.DateTimeField(auto_now=True)  # 时间类型字段,会显示注册时间
    class Meta:  # 更改表明 固定格式
        db_table = 'user'
