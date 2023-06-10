import uuid
from django.core.mail import send_mail
from mycelery.main import app
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
import redis


@app.task
def send_sms(email, uid):
    token = str(uuid.uuid4()).replace('-', '')
    uidb64 = urlsafe_base64_encode(force_bytes(uid))
    url = 'http://127.0.0.1:8000/class/activate?uid=%s&token=%s'%(uidb64,token)
    conn = redis.StrictRedis(host="127.0.0.1", port=6379, password="", db=3)
    conn.set(uid, token, ex=180)
    EMAIL_HOST_USER = '3052573970@qq.com'
    subject = '班级云服务平台邮箱激活'
    html_message = '<p>用户您好</p>' \
                   '<p>感谢您使用班级云服务平台</p>' \
                   '<p>您的邮箱为：%s。请点击此连接激活您的邮箱,链接有效期为三分钟，请尽快激活!</p>' \
                   '<p><a href="%s">%s</a></p>' % (email, url, url)
    send_status=send_mail(subject, '班级云服务平台邮箱激活', EMAIL_HOST_USER, [email],html_message=html_message)

    return send_status

@app.task
def send_pass(email, uid):
    token = str(uuid.uuid4()).replace('-', '')
    uidb64 = urlsafe_base64_encode(force_bytes(uid))
    url = 'http://127.0.0.1:8000/class/modify?uid=%s&token=%s'%(uidb64,token)
    conn = redis.StrictRedis(host="127.0.0.1", port=6379, password="", db=3)
    conn.set(uid, token, ex=180)
    EMAIL_HOST_USER = '3052573970@qq.com'
    subject = '班级云服务平台密码服务'
    html_message = '<p>用户您好</p>' \
                   '<p>感谢您使用班级云服务平台</p>' \
                   '<p>您的邮箱为：%s。请点击此连接以此修改您的密码,链接有效期为三分钟，请尽快激活链接!</p>' \
                   '<p><a href="%s">%s</a></p>' % (email, url, url)
    send_status=send_mail(subject, '班级云服务平台密码服务', EMAIL_HOST_USER, [email],html_message=html_message)

    return send_status

@app.task
def send_email(email, uid):
    token = str(uuid.uuid4()).replace('-', '')
    uidb64 = urlsafe_base64_encode(force_bytes(uid))
    url = 'http://127.0.0.1:8000/class/changeemail?uid=%s&token=%s'%(uidb64,token)
    conn = redis.StrictRedis(host="127.0.0.1", port=6379, password="", db=3)
    conn.set(uid, token, ex=180)
    EMAIL_HOST_USER = '3052573970@qq.com'
    subject = '班级云服务平台邮箱服务'
    html_message = '<p>用户您好</p>' \
                   '<p>感谢您使用班级云服务平台</p>' \
                   '<p>您的邮箱为：%s。请点击此连接以此更改您的邮箱,链接有效期为三分钟，请尽快激活链接!</p>' \
                   '<p><a href="%s">%s</a></p>' % (email, url, url)
    send_status=send_mail(subject, '班级云服务平台邮箱服务', EMAIL_HOST_USER, [email],html_message=html_message)

    return send_status

@app.task
def send_repass(email, uid):
    token = str(uuid.uuid4()).replace('-', '')
    uidb64 = urlsafe_base64_encode(force_bytes(uid))
    url = 'http://127.0.0.1:8000/class/changepass?uid=%s&token=%s'%(uidb64,token)
    conn = redis.StrictRedis(host="127.0.0.1", port=6379, password="", db=3)
    conn.set(uid, token, ex=180)
    EMAIL_HOST_USER = '3052573970@qq.com'
    subject = '班级云服务平台密码服务'
    html_message = '<p>用户您好</p>' \
                   '<p>感谢您使用班级云服务平台</p>' \
                   '<p>您的邮箱为：%s。请点击此连接以此更改您的密码,链接有效期为三分钟，请尽快激活链接!</p>' \
                   '<p><a href="%s">%s</a></p>' % (email, url, url)
    send_status=send_mail(subject, '班级云服务平台密码服务', EMAIL_HOST_USER, [email],html_message=html_message)

    return send_status

# @app.task
# def send_sms(email, uid):
#     token = str(uuid.uuid4()).replace('-', '')
#     uidb64 = urlsafe_base64_encode(force_bytes(uid))
#     url = 'https://71i667r990.goho.co/class/activate?uid=%s&token=%s'%(uidb64,token)
#     conn = redis.StrictRedis(host="127.0.0.1", port=6379, password="", db=3)
#     conn.set(uid, token, ex=180)
#     EMAIL_HOST_USER = '3052573970@qq.com'
#     subject = '班级云服务平台邮箱激活'
#     html_message = '<p>用户您好</p>' \
#                    '<p>感谢您使用班级云服务平台</p>' \
#                    '<p>您的邮箱为：%s。请点击此连接激活您的邮箱,链接有效期为三分钟，请尽快激活!</p>' \
#                    '<p><a href="%s">%s</a></p>' % (email, url, url)
#     send_status=send_mail(subject, '班级云服务平台邮箱激活', EMAIL_HOST_USER, [email],html_message=html_message)
#
#     return send_status
#
# @app.task
# def send_pass(email, uid):
#     token = str(uuid.uuid4()).replace('-', '')
#     uidb64 = urlsafe_base64_encode(force_bytes(uid))
#     url = 'https://71i667r990.goho.co/class/modify?uid=%s&token=%s'%(uidb64,token)
#     conn = redis.StrictRedis(host="127.0.0.1", port=6379, password="", db=3)
#     conn.set(uid, token, ex=180)
#     EMAIL_HOST_USER = '3052573970@qq.com'
#     subject = '班级云服务平台密码服务'
#     html_message = '<p>用户您好</p>' \
#                    '<p>感谢您使用班级云服务平台</p>' \
#                    '<p>您的邮箱为：%s。请点击此连接以此修改您的密码,链接有效期为三分钟，请尽快激活链接!</p>' \
#                    '<p><a href="%s">%s</a></p>' % (email, url, url)
#     send_status=send_mail(subject, '班级云服务平台密码服务', EMAIL_HOST_USER, [email],html_message=html_message)
#
#     return send_status
#
# @app.task
# def send_email(email, uid):
#     token = str(uuid.uuid4()).replace('-', '')
#     uidb64 = urlsafe_base64_encode(force_bytes(uid))
#     url = 'https://71i667r990.goho.co/class/changeemail?uid=%s&token=%s'%(uidb64,token)
#     conn = redis.StrictRedis(host="127.0.0.1", port=6379, password="", db=3)
#     conn.set(uid, token, ex=180)
#     EMAIL_HOST_USER = '3052573970@qq.com'
#     subject = '班级云服务平台邮箱服务'
#     html_message = '<p>用户您好</p>' \
#                    '<p>感谢您使用班级云服务平台</p>' \
#                    '<p>您的邮箱为：%s。请点击此连接以此更改您的邮箱,链接有效期为三分钟，请尽快激活链接!</p>' \
#                    '<p><a href="%s">%s</a></p>' % (email, url, url)
#     send_status=send_mail(subject, '班级云服务平台邮箱服务', EMAIL_HOST_USER, [email],html_message=html_message)
#
#     return send_status
#
# @app.task
# def send_repass(email, uid):
#     token = str(uuid.uuid4()).replace('-', '')
#     uidb64 = urlsafe_base64_encode(force_bytes(uid))
#     url = 'https://71i667r990.goho.co/class/changepass?uid=%s&token=%s'%(uidb64,token)
#     conn = redis.StrictRedis(host="127.0.0.1", port=6379, password="", db=3)
#     conn.set(uid, token, ex=180)
#     EMAIL_HOST_USER = '3052573970@qq.com'
#     subject = '班级云服务平台密码服务'
#     html_message = '<p>用户您好</p>' \
#                    '<p>感谢您使用班级云服务平台</p>' \
#                    '<p>您的邮箱为：%s。请点击此连接以此更改您的密码,链接有效期为三分钟，请尽快激活链接!</p>' \
#                    '<p><a href="%s">%s</a></p>' % (email, url, url)
#     send_status=send_mail(subject, '班级云服务平台密码服务', EMAIL_HOST_USER, [email],html_message=html_message)
#
#     return send_status
