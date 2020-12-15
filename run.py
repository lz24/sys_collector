#!/usr/bin/env python
# coding=utf-8

# Author: ymc023
# Mail:
# Platform: python2.x.x && python3.x.x
# Date:Wed 14 Jun 2017 11:44:26 AM CST

import sys
import logging
import logging.config
import ConfigParser
import json
import time
import datetime
import random
import urllib2

sys.path.append('/usr/local/sys_collector')
try:
    logging.config.fileConfig("/usr/local/sys_collector/sys_collector.conf")
    log = logging.getLogger("sys_collector")
    cf = ConfigParser.ConfigParser()
    cf.read('/usr/local/sys_collector/sys_collector.conf')
except BaseException:
    log.error('配置文件读取错误!')
    sys.exit(0)

try:
    from sys_collector import collector as c

except BaseException:
    log.error('初始化调用collector错误!')
    sys.exit(0)

try:
    postpriv = {
        'username': '%s' % cf.get(
            'dispatch',
            'username'),
        'password': '%s' % (cf.get(
            'dispatch',
            'password'))}
    time_delay = cf.get('dispatch', 'time_delay')
    exec_time = cf.get('dispatch', 'time')
    index_url = cf.get('dispatch', 'index')
except BaseException:
    log.error('获取调度时间出错!')
    sys.exit(0)


while True:
    try:
        now = int(datetime.datetime.now().strftime('%H'))
        h = int(exec_time) - now
        if h < 0:
            hold = (24 - abs(h)) * 3600
        elif h > 0:
            hold = h * 3600
        else:
            hold = 0
        time.sleep(hold)
        if hold == 0:
            services = c.CollectorServices()
            base = c.CollectorBase()
            basedata = dict(base.info, **services.info)
            try:
                alldata = dict(postpriv, **basedata)
                jsondata = json.dumps(alldata)
            except BaseException:
                log.error('data collecotr error!')
            delay = random.randrange(int(time_delay))
            time.sleep(delay)
            try:
                res = c._post(index_url, jsondata)
                if res == 'True':
                    log.info('send:%s' % basedata)
                else:
                    log.error('Post return error!')
            except urllib2.HTTPError as e:
                log.error(e)
            time.sleep(3600 - delay)
    except BaseException:
        log.error('获取执行时间出错!')
