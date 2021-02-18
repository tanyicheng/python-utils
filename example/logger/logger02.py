import logging

# 输出日志到文件
logging.basicConfig(level=logging.DEBUG,  # 设置日志显示级别
                    format='%(asctime)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%A, %d %B %Y %H:%M:%S',  # 指定日期时间格式
                    filename='sos.log',  # 指定日志存储的文件及位置
                    filemode='w',  # 文件打开方式
                    )  # 指定handler使用的日志显示格式
import logging

logging.debug('Debug状态')
logging.info('输入状态')
logging.warning('警告级别错误')
logging.error('产生错误信息')
logging.critical('产生严重错误')

# 结果
# Thursday, 25 January 2018 17:10:38[line:47] DEBUG Debug状态
# Thursday, 25 January 2018 17:10:38[line:48] INFO 输入状态
# Thursday, 25 January 2018 17:10:38[line:49] WARNING 警告级别错误
# Thursday, 25 January 2018 17:10:38[line:50] ERROR 产生错误信息
# Thursday, 25 January 2018 17:10:38[line:51] CRITICAL 产生严重错误
