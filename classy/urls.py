from django.urls import path,re_path
from classy import views
from django.conf.urls import handler404

urlpatterns = [
    path('admin/', views.index),
    path('login/',views.login_view),
    path('task_list/',views.task_list),
    path('role/',views.role),
    path('upload/',views.upload,name='upload'),
    path('password/',views.password),
    path('register/',views.register),
    path('committee/',views.committee),
    path('help/',views.help),
    path('welcome/',views.welcome),
    path('log/',views.log),
    path('feedback/',views.feedback),
    path('form/',views.form),
    path('getfile/',views.getfile,name='getfile'),
    path('error/',views.error),
    re_path(r'^activate/$',views.activate,name='activate'),
    path('task_upload/',views.task_uplaod),
    path('describe/',views.describe),
    path('send/',views.send_zip),
    path('change/',views.changestatus),
    path('queue/',views.queue),
    path('only/',views.only),
    path('add/',views.add),
    re_path(r'^modify/$', views.modify, name='modify'),
    re_path(r'^changeemail/$', views.changeemail, name='changeemail'),
    re_path(r'^changepass/$',views.changepass,name='changepass'),
]
