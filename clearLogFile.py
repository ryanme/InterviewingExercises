#! coding:utf8

"""
    写一个清理日志的脚本，每次运行就把三天之前的日志删除，日志名的格式是xxx-20170623.log
"""

import os
from datetime import datetime, timedelta
import re
import logger

now = datetime.now().strftime('%Y%m%d')
three_days_ago = datetime.strptime(now, '%Y%m%d') + timedelta(days=-3)
logger.logger.info('三天前的时间为:%s' % three_days_ago)

dirname = "/Users/ryan/Documents/Python Project/TestDemo/log/"
file_list = os.listdir(dirname)
will_removelist = []
fail_removelist = []
save_list = []

def clear_log():
    for i in file_list:
        searchObj = re.search(r'^xxx-(\d)(\d)(\d)(\d)(\d)(\d)(\d)(\d).log$', i)
        if searchObj:
            logname = searchObj.group()
            timeString = re.findall(r"^xxx-(.+?).log$", logname)[0]
            time = datetime.strptime(timeString, '%Y%m%d')
            if time < three_days_ago:
                full_path = dirname + i
                try:
                    os.remove(full_path)
                    will_removelist.append(i)
                except:
                    fail_removelist.append(i)
            else:
                save_list.append(i)

    logger.logger.info('以下文件被清理: %s' % will_removelist)
    logger.logger.info('以下文件清理失败: %s' % fail_removelist)
    logger.logger.info('以下文件未被删除: %s' % save_list)


if __name__ == '__main__':
    clear_log()


