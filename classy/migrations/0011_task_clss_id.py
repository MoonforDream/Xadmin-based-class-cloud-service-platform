# Generated by Django 3.2.16 on 2023-06-03 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classy', '0010_remove_userinfo_is_stu'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='clss_id',
            field=models.CharField(db_column='class_id', default='', max_length=255, verbose_name='班级编号'),
        ),
    ]