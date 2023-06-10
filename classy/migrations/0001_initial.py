# Generated by Django 3.2.16 on 2023-05-31 15:38

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stu_user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stu_id', models.CharField(db_column='stu_id', default=None, max_length=255, verbose_name='学号')),
                ('stu_account', models.CharField(db_column='stu_account', default=None, max_length=255, verbose_name='学生帐号')),
                ('stu_pass', models.CharField(db_column='stu_pass', default=None, max_length=255, verbose_name='密码')),
                ('stu_class', models.CharField(db_column='stu_class', default=None, max_length=255, verbose_name='班级名称')),
                ('stu_work', models.CharField(db_column='stu_work', default='学生', max_length=255, verbose_name='学生职位')),
                ('class_num', models.CharField(db_column='class_num', default=None, max_length=255, verbose_name='班级编号')),
                ('stu_email', models.CharField(db_column='stu_email', default='无', max_length=255, verbose_name='学生邮箱')),
            ],
            options={
                'db_table': 'Stu_user',
            },
        ),
        migrations.CreateModel(
            name='task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_id', models.CharField(db_column='task_id', default=None, max_length=255, verbose_name='任务编号')),
                ('task_type', models.CharField(db_column='task_type', default=None, max_length=255, verbose_name='任务类型')),
                ('task_start', models.DateTimeField(auto_now_add=True, db_column='task_start', verbose_name='任务开始时间')),
                ('task_end', models.DateTimeField(db_column='task_end', default=None, verbose_name='任务截止时间')),
                ('task_name', models.CharField(db_column='task_name', default='签到', max_length=255, verbose_name='任务名')),
                ('task_file', models.FileField(upload_to='uploads/')),
                ('task_status', models.CharField(db_column='task_status', default='进行中', max_length=255, verbose_name='任务状态')),
                ('task_feedback', models.TextField(db_column='task_feedback', default='无', verbose_name='任务数据反馈')),
            ],
            options={
                'db_table': 'task',
            },
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('class_num', models.CharField(db_column='class_num', default=None, max_length=255, verbose_name='班级编号')),
                ('stu_class', models.CharField(db_column='stu_class', default=None, max_length=255, verbose_name='班级名称')),
                ('stu_num', models.CharField(db_column='stu_num', default=0, max_length=255, verbose_name='班级人数')),
                ('stu_work', models.CharField(db_column='stu_work', default='学生', max_length=255, verbose_name='学生职位')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'db_table': 'UserInfo',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
