# Generated by Django 3.2.16 on 2023-06-06 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classy', '0019_auto_20230606_1113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='task_start',
            field=models.DateTimeField(db_column='task_start', default='2023-06-06 11:13:32', verbose_name='任务开始时间'),
        ),
    ]