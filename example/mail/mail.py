import yagmail

# 链接邮箱服务器  （邮箱地址,授权码，主机地址）
yag = yagmail.SMTP(user="xiaoyifam@163.com", password="xiaoyi891126", host='smtp.163.com')

# 邮箱正文
contents = ['This is the body, and here is just text http://somedomain/image.png',
            'You can find an audio file attached.', '/local/path/song.mp3']

# 发送邮件
yag.send(
    to=['65797706@qq.com', 'yuejiao.xu@seraphim-energy.com'],  # 如果多个收件人的话，写成list就行了，如果只是一个账号，就直接写字符串就行to='123@qq.com'
    cc='yicheng.tan@seraphim-energy.com',  # 抄送
    subject='学习发送邮件',  # 邮件标题
    contents='你好，你今天开心吗？',  # 邮件正文
    # attachments=[r'd://log.txt', r'd://baidu_img.jpg']
)  # 附件如果只有一个的话，用字符串就行，attachments=r'd://baidu_img.jpg'

# 可简写成：
# yag.send('65797706@qq.com', '发送附件', contents, ["E://Temp//test.log", "e://Temp//sos.log"])

# 关闭
yag.close()
