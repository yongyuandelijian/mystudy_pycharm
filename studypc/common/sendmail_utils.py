# 发送邮件的方法
# 需要可以添加附件，还需要可以超过大小进行压缩，还需要可以删除自己产生的临时文件
# 发送邮件必须要先检查sendmail服务是否开启，如果没有安装服务，需要先进行安装

import smtplib
from email.mime.text import MIMEText # 对邮件文本进行设置
from email.header import Header
from email.mime.application import MIMEApplication   # 用于增加附件,增加附件必须先设置多个部分
import email.mime.multipart
# import sys


def bj_sendmail():
    # fromaddr="lipengchao<1223036184@qq.com>"  # 这样是发不出去的  mail_user+"<"+mail_user+"@"+mail_postfix+">"
    fromaddr = "from@runoob.com"
    toaddr = ["1028986374@qq.com"]  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
    zfbm = "utf-8"

    # 三个参数分别是文本内容，文本格式，字符编码
    message = MIMEText("程序自动发来的测试邮件的内容，哈哈哈", "plain", zfbm)
    message["From"] = Header("fasong", zfbm)
    message["To"] = Header("jieshou", zfbm)

    subject = "smtp测试邮件主题"  # 预览标题乱码和这里没关系
    message["subject"] = Header(subject, zfbm)

    result='没有结果'
    try:
        ｓmtp_object = smtplib.SMTP('localhost',25)
        ｓmtp_object.sendmail(from_addr=fromaddr, to_addrs=toaddr, msg=message.as_string())
        result = "邮件发送成功！！！"
    except smtplib.SMTPException:
        result = "发送邮件错误！！！"

    # smtp_object=smtplib.SMTP(host="127.0.0.1",port=25,local_hostname="localhost")  # 获取一个SMTP对象
    #
    # SMTP.sendmail(from_addr=fromaddr,to_addrs=toaddr,msg=message)
    return result

def wl_sendmail(to_addrlist):
    result="没有结果"
    # 第三方ＳＭＴＰ服务
    mail_host="smtp.qq.com"    # 设置服务器
    mail_user="1028986374"     # 用户名
    mail_pass="arpcxxbhvdvobejg";    # 密码如果是ｑｑ必须使用单独授权的密码，无法使用本身的ｑｑ邮箱密码
    text_format="plain";   # 文本格式
    main_type="qq.com"
    encoding="utf-8";  # 邮件总体字符编码

    from_addr=mail_user+"<"+mail_user+"@"+main_type+">"   #发送人 格式就是账号《账号＠邮箱类型》
    to_addrlist=["1264699937@qq.com","rosiel5973@vip.qq.com","1223036184@qq.com"];  # 目标列表
    print(to_addrlist[2]);
    subject="测试邮件主体";
    content="早上好，附件是一张励志桌面图片，送给你，希望你喜欢。另外　iPhone XS Max 512GB 售价高达 12799 元。"   # 这样并不能影响发送邮件内的格式

    # sys.setdefaultencoding(encoding); 不可用
    # if not isinstance(subject,unicode):
    #     subject=unicode(subject);

    message=MIMEText(str(content),text_format,encoding);
    message["From"]=Header(from_addr,encoding);
    message["subject"] = Header(subject, encoding);

    try:
        mail_object=smtplib.SMTP();
        mail_object.connect(mail_host,25);
        mail_object.login(mail_user,mail_pass);
        for i in range(len(to_addrlist)):
            message["To"] = Header(to_addrlist[i], encoding);
            print("现在要发送的地址是：",to_addrlist[i])
            mail_object.sendmail(from_addr=from_addr, to_addrs=to_addrlist[2], msg=message.as_string());
        result="邮件发送成功";
    except smtplib.SMTPException as e:
        print(e);
        result="邮件发送失败！！！";


    return result;


# 带附件的发送  发送列表，附件路径

def wlfj_sendmail(to_addrlist,filepath,subject="测试邮件主体",content="邮件正文"):
    result="没有结果";
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


if __name__ == '__main__':
    # print(bj_sendmail());
    to_addrlist = ["Rosiel5973@163.com", "Rosiel5973@gmail.com", "897398197@qq.com"];  # 目标列表
    # print(wl_sendmail(to_addrlist));
    content = "早上好，附件是一张励志桌面图片，送给你，希望你喜欢。另外　刚刚发布的iPhone XS Max 512GB 售价 12799 元。"  # 这里换行并不能影响发送邮件内的格式
    file_path="/media/lipengchao/study/pycharmproject/studypc/common/img/jianchi.jpg";
    print(wlfj_sendmail(to_addrlist,file_path))
    # b=repr("\xc7\xeb\xca\xb9\xd3\xc3\xca\xda\xc8\xa8\xc2\xeb\xb5\xc7\xc2\xbc\xa1\xa3\xcf\xea\xc7\xe9\xc7\xeb\xbf\xb4");
    # print(b.encode().decode())