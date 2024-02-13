# 开发者：Pabi
# 开发时间：2023/1/24 16:11
import requests
import json
import re
import csv

with open('reptiles.csv', 'w', encoding='ANSI', newline='') as filename:
    csvwriter = csv.DictWriter(filename, fieldnames=[])
    csvwriter.writeheader()
    url = 'http://43.139.182.137:48080/admin-api/system/user/page?pageNo=1&pageSize=10'
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN, zh;q=0.9',
        'Authorization': 'Bearer 91f2520fc850496bb833288fd297c6e9',
        'Connection': 'keep-alive',
        'Cookie': 'remember-me=YWRtaW46MTY3NTY3MTU1MDUwMDo0MThiYmE2ZWMyMTAzNzVlNmZmNDIyZmViOWIwODE5YTk3MzljODRmM2YzNDkxYWQ2NTFlZjUzMzk1NWVjMjYy;jenkins-timestamper-offset=-28800000; JSESSIONID.4ec43e05=node0dtqoa3eazqnd1q1jv1n0x9s7m168.node0; Hm_lvt_fadc1bd5db1a1d6f581df60a1807f8ab=1674478063,1674539422,1674574144,1674662141;Hm_lpvt_fadc1bd5db1a1d6f581df60a1807f8ab=1674662141',
        'Host': '43.139.182.137:48080',
        'Referer': 'http://43.139.182.137:48080/admin-ui/system/user',
        'tenant-id': '1',
        'User-Agent': 'Mozilla/5.0(Windows NT 10.0;Win64; x64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
    }
    res = requests.get(url=url, headers=headers)
    text_res = res.text
    # re.findall是正则表达式
    html_data = re.findall(r'"data":{"list":.*,"total":14},"msg":""}', res.text, flags=0)[0]
    # json.loads转成字典
    list_data = json.loads(html_data)
    # 字典取值
    data = list_data['mods']['itemlist']['data']['auctions']

    for index in data:
        dict = {
            '标题': index['raw_title'],
            '标题': index['raw_title'],
            '标题': index['raw_title'],
            '标题': index['raw_title'],
            '标题': index['raw_title'],
            '标题': index['raw_title']
        }
        csvwriter.writerow(dict)
        print(dict)

