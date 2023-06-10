# Generated by Django 3.2.16 on 2023-06-06 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classy', '0017_auto_20230606_1023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='describe',
            field=models.TextField(db_column='describe', default='', verbose_name='作业描述'),
        ),
        migrations.AlterField(
            model_name='task',
            name='task_start',
            field=models.DateTimeField(db_column='task_start', default='2023-06-06 10:58:02', verbose_name='任务开始时间'),
        ),
    ]
