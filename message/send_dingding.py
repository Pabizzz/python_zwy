# 开发者：Pabi
# 开发时间：2023/1/23 23:20
import os

import requests
from jenkins import Jenkins

jenkins_url = 'http://43.139.182.137:8090/'
server = Jenkins(jenkins_url, username='admin', password='admin')
job_name = 'job/ApiTest'
job_url = server.get_info(job_name)['url']
job_last_number = server.get_info(job_name)['lastBuild']['number']
report_url = job_url + str(job_last_number) + 'allure'

def push_message():
    content = {}
    pwd = os.path.dirname(os.getcwd())
    new_path = pwd.replace('\\', '/')
    file_path = new_path + '/allure-report/export/prometheusData.txt'
    f = open(file_path)
    # readlines()是读多行的意思。是多行
    for line in f.readlines():
        # 通过空格分割，分别拿前后的字符串
        # strip()是去除字符串，split()是分割字符串
        launch_name = line.strip('\n').split(' ')[0]
        num = line.strip('\n').split(' ')[1]
        content.update({launch_name: num})
    f.close()

    passed_num = content['launch_status_passed']  # 通过数量
    broken_num = content['launch_status_broken']  # 失败数量
    skipped_num = content['launch_status_skipped']  # 阻塞数量
    failed_num = content['launch_status_failed']  # 跳过数量
    retries_run_num = content['launch_retries_run']  # 总数量

    '''
    钉钉消息发送，通过webhook发送消息
    webhook是钉钉发送消息的地址
    '''
    webhook = 'xxx'
    content_dingding = {
        "mdgtype": "text",
        "text": {
            "content": "接口自动化脚本执行结果: "
            "\n运行总数" + retries_run_num
            + "\n通过数量" + passed_num
            + "\n失败数量" + failed_num
            + "\n阻塞数量" + broken_num
            + "\n跳过数量" + skipped_num
            + "\n构建地址： \n" + job_url
            + "\n报告地址： " + report_url
        }
    }
    requests.post(url=webhook, json=content_dingding, verify=False)




push_message()