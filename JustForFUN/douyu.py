# -*- coding: utf-8 -*-
import os
import string
from time import sleep
import requests
"""
    斗鱼关注通知
"""

def send_email(SUBJECT):
    import smtplib
    mail_user = "188888888@wo.cn"
    mail_pwd = "88888"
    FROM = '188888888@wo.cn'
    TO = ['188888888@wo.cn']  # must be a list
    TEXT = SUBJECT

    # Prepare actual message
    message = """\From: %s\nTo: %s\nSubject: %s\n\n%s
           """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    try:
        #server = smtplib.SMTP(SERVER)
        server = smtplib.SMTP("smtp.wo.cn", 25)
        # server.ehlo()
        # server.starttls()
        server.login(mail_user, mail_pwd)
        server.sendmail(FROM, TO, message)
        # server.quit()
        server.close()
        print 'successfully sent the mail'
    except Exception, e:
        print str(e)


while 1:
    try:
        url = "http://www.douyutv.com/erke"
        r = requests.get(url, timeout=10, verify=False)
        if "feedback_report_button" in r.text:
            send_email("erke")
            sleep(11000)
        sleep(100)
    except Exception, e:
        print str(e)
        sleep(1)
