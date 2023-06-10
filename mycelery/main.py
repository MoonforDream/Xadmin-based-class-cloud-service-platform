import os
from celery import Celery

app=Celery('email')

os.environ.setdefault('DJANGO_SETTINGS_MODULE','HelloWorld.settings')

import django
django.setup()
app.config_from_object('mycelery.config')

app.autodiscover_tasks(["mycelery.email",])

#启动Celery的命令
#强烈建议切换目录到mycelery根目录下启动
#celery -A mycelery.main worker --loglevel=info