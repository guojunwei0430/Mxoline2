# encoding: utf-8
from random import Random

__author__ = 'mtianyan'
__date__ = '2018/1/11 0010 10:47'
from  users.models import EmailVerifyRecord

from django.core.mail import send_mail,EmailMessage

#from Mxonline2.settings import EMAIL_FROM

from django.template import loader

EMAIL_FROM = '1321751652@qq.com'

def random_str(random_length=8):
    str = ''

    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars) - 1
    random = Random()
    for i in range(random_length):
        str += chars[random.randint(0, length)]
    return str


def send_register_eamil(email, send_type="register"):

    email_record = EmailVerifyRecord()

    code = random_str(16)
    email_record.code = code
    email_record.email = email
    email_record.send_type = send_type

    email_record.save()


    email_title = ""
    email_body = ""

    if send_type == "register":
        email_title = "mtianyan慕课小站 注册激活链接"
        email_body = "请点击下面的链接激活你的账号: http://127.0.0.1:8000/active/{0}".format(code)

        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            pass
    elif send_type == "forget":
        email_title = "mtianyan慕课小站 找回密码链接"
        email_body = loader.render_to_string(
            "email_forget.html",
            {
                "active_code": code
            }
        )
        msg = EmailMessage(email_title, email_body, EMAIL_FROM, [email])
        msg.content_subtype = "html"
        send_status = msg.send()





