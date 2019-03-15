# coding:utf-8
import psycopg2
import logging
import datetime
import time
import threading

import hashlib
import os
import re
import urllib.request
from bs4 import BeautifulSoup

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s-%(threadName)s-%(name)s-%(funcName)s-%(levelname)s-%(message)s')
logger = logging.getLogger(__name__)

isruning = True
interval = 5


def controlthread_body():
    '''控制线程整体函数'''
    global interval, isruning

    while isruning:
        i = input('输入byte终止爬虫，输入数字改变爬虫工作时间间隔，单位秒：')
        logger.info('控制输入{0}'.format(i))
        try:
            interval = int(i)
        except ValueError:
            if i.lower() == 'byte':
                isruning = False


def isthreadtime():
    '''判断工作时间'''
    now = datetime.datetime.now()
    df = '%H%M%S'
    strnow = now.strftime(df)
    starttime = datetime.time(9, 30).strftime(df)
    endtime = datetime.time(15, 30).strftime(df)
    if now.weekday() == 5 or now.weekday() == 6 \
            or (strnow < starttime or strnow > endtime):
        return False
    return True


def workthread_body():
    global interval, isruning
    while isruning:
        if isthreadtime():
            logger.info('交易时间，爬虫休眠一小时')
            time.sleep(60 * 60)
            continue
        logger.info('爬虫开始工作')
        '''操作数据'''
        logger.info('爬虫休眠{0}'.format(interval))
        time.sleep(interval)


def main():
    '''主函数'''
    global interval, isruning
    workthread = threading.Thread(target=workthread_body, name='WorkThread')
    workthread.start()

    controlthread = threading.Thread(target=controlthread_body, name='ControlThread')
    controlthread.start()


def insert_hisq_data(row):
    connection = psycopg2.connect(host='localhost', user='postgres', password='111111', database='test', port='5432',
                                  charset='utf-8')
    row['name'] = 'test'
    try:
        with connection.cursor() as cur:
            sql = 'insert into app_user(name) values (%s)'
            cur.execute(sql, row)
            connection.commit()
    except psycopg2.DatabaseError as error:
        connection.rollback()
    finally:
        connection.close()


if __name__ == '__main__':
    main()
