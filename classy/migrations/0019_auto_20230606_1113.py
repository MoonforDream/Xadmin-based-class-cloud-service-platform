# Generated by Django 3.2.16 on 2023-06-06 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classy', '0018_auto_20230606_1058'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='send_name',
            field=models.CharField(db_column='send_name', default='', max_length=255, verbose_name='发布人'),
        ),
        migrations.AlterField(
            model_name='task',
            name='task_start',
            field=models.DateTimeField(db_column='task_start', default='2023-06-06 11:13:26', verbose_name='任务开始时间'),
        ),
    ]