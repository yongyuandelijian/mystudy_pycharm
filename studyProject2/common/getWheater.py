import smtplib
from email.mime.text import MIMEText # 对邮件文本进行设置
from email.header import Header
from email.mime.application import MIMEApplication   # 用于增加附件,增加附件必须先设置多个部分
import email.mime.multipart
import datetime
import json
import requests

# 利用城市获取天气
def hqtq():
    response = requests.get("http://wthrcdn.etouch.cn/weather_mini?city=西安")
    response.encoding = "utf-8"
    # print(type(response.text),response.text)
    tq = json.loads(response.text)
    tq = tq.get("data")

    mailContent="城市:{city}\n空气指数：{aqi}\n感冒建议：{ganmao}\n当前温度:{wendu}\n"\
        .format(city=tq.get("city"),aqi=tq.get("aqi"),ganmao=tq.get("ganmao"),wendu=tq.get("wendu"))

    wtyb = tq.get("forecast");
    yb=""
    for mt in wtyb:
        fl = mt.get("fengli")
        fl = fl[fl.index("[", 6, len(fl)):fl.index("]", 6, len(fl)) + 1]
        s = "日期：{date}\t\t\t{type}\t\t\t最高温度：{high}\t\t\t最低温度：《{low}》\t\t\t风力：{fengli}\t\t\t风向：{fengxiang}\n" \
            .format(date=mt.get("date"), type=mt.get("type"), high=mt.get("high"), low=mt.get("low"), fengli=fl,
                    fengxiang=mt.get("fengxiang"))
        yb=yb+s

    mailContent=mailContent+"\n\n下面是五天的天气预报：\n"+yb
    return mailContent

# 注册成功发送邮件

def wlfj_sendmail(to_addrlist,filepath,subject="邮件主体",content="邮件正文"):
    result="";
    # 第三方ＳＭＴＰ服务
    mail_host="smtp.qq.com";    # 设置服务器
    mail_user="1028986374";     # 用户名
    mail_pass="krpykfwxuazkbegc";    # 密码如果是ｑｑ必须使用单独授权的密码，无法使用本身的ｑｑ邮箱密码
    text_format="plain";   # 文本格式
    main_type="qq.com"
    encoding="utf-8";  # 邮件总体字符编码

    from_addr=mail_user+"<"+mail_user+"@"+main_type+">"   #发送人 格式就是账号《账号＠邮箱类型》

    # 设置内容为multipart
    message=email.mime.multipart.MIMEMultipart();

    content_txt=email.mime.text.MIMEText(str(content),text_format,encoding);
    message["From"]=Header(from_addr,encoding);
    message["subject"] = Header(subject, encoding);
    message.attach(content_txt); # 追加文字部分
    # 添加附件
    part=MIMEApplication(open(filepath,'rb').read());
    part.add_header("Content-Disposition","attachment",filename="jianchi.jpg");
    message.attach(part);   # 追加附件部分

    mail_object = smtplib.SMTP();
    try:
        mail_object.connect(mail_host,25);
        mail_object.login(mail_user,mail_pass);
        for i in range(len(to_addrlist)):
            message["To"] = Header(to_addrlist[i], encoding);
            print("现在要发送的地址是：",to_addrlist[i])
            mail_object.sendmail(from_addr=from_addr, to_addrs=to_addrlist[i], msg=message.as_string());
        result="邮件发送成功";
    except smtplib.SMTPException as e:
        print(e);
        result="邮件发送失败！！！";
    finally:
        mail_object.quit();

    return result;