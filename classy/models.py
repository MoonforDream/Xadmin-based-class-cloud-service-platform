
from django.contrib.auth.hashers import check_password
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


# Create your models here.

class UserInfo(AbstractUser):
    class Meta:
        db_table="UserInfo"

    class_num=models.CharField(default='',verbose_name='班级编号',db_column='class_num',max_length=255)
    stu_class = models.CharField(default='', verbose_name="班级名称", db_column='stu_class', max_length=255)
    stu_work = models.CharField(default='学生', verbose_name="学生职位", db_column="stu_work", max_length=255)
    stu_name = models.CharField(default='', verbose_name="学生姓名", db_column='stu_name', max_length=255)
    stunum=models.CharField(default='',verbose_name="班级序号",db_column='stunum',max_length=255)
    stu_id=models.CharField(default='',verbose_name='学号',db_column='stu_id',max_length=255)
    stu_task = models.TextField(default='', verbose_name='学生已完成任务编号', db_column='stu_task')

class Stu_user(models.Model):
    class Meta:
        db_table="Stu_user"

    stu_id=models.CharField(default='',verbose_name="学号",db_column='stu_id',max_length=255)
    stu_account=models.CharField(default='',verbose_name="学生帐号",db_column='stu_account',max_length=255)
    stu_class=models.CharField(default='',verbose_name="班级名称",db_column='stu_class',max_length=255)
    stu_work=models.CharField(default='学生',verbose_name="学生职位",db_column="stu_work",max_length=255)
    class_num = models.CharField(default='', verbose_name='班级编号', db_column='class_num', max_length=255)
    stu_email=models.CharField(default='无',verbose_name="学生邮箱",db_column='stu_email',max_length=255)
    stu_name=models.CharField(default='',verbose_name="学生姓名",db_column='stu_name',max_length=255)
    stu_status=models.CharField(default='已启用',verbose_name="学生状态",db_column='stu_status',max_length=255)
    stu_task=models.TextField(default='',verbose_name='学生已完成任务编号',db_column='stu_task',max_length=255)
    stunum=models.CharField(default='',verbose_name='班级序号',db_column='stunum',max_length=255)


class task(models.Model):
    class Meta:
        db_table="task"

    task_id=models.CharField(default=None,verbose_name="任务编号",db_column='task_id',max_length=255)
    task_type=models.CharField(default=None,verbose_name="任务类型",db_column='task_type',max_length=255)
    task_start=models.DateTimeField(default=timezone.now().strftime("%Y-%m-%d %H:%M:%S"),verbose_name="任务开始时间",db_column='task_start')
    task_end=models.DateTimeField(default=None,verbose_name="任务截止时间",db_column='task_end')
    task_name=models.CharField(default='签到',verbose_name="任务名",db_column='task_name',max_length=255)
    task_file=models.TextField(default='',verbose_name='任务附件地址',db_column='task_file')
    task_status=models.CharField(default='进行中',verbose_name="任务状态",db_column='task_status',max_length=255)
    task_feedback=models.TextField(default='无',verbose_name="任务数据反馈",db_column='task_feedback')
    lat=models.FloatField(default=0,verbose_name="签到纬度",db_column='lat')
    lon=models.FloatField(default=0,verbose_name="签到经度",db_column='lon')
    radius=models.FloatField(default=0,verbose_name='签到范围',db_column='radius')
    clss_id=models.CharField(default='',verbose_name='班级编号',db_column='class_id',max_length=255)
    describe=models.TextField(default='',verbose_name='作业描述',db_column='describe')
    send_name=models.CharField(default='',verbose_name='发布人',db_column='send_name',max_length=255)