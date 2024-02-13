# 开发者：Pabi
# 开发时间：2023/1/26 0:40
"""
爬取“最好大学网”排行
"""

import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Opera/9.80 (Windows NT 6.0) Presto/2.12.388 Version/12.14"
}
response = requests.get("http://www.zuihaodaxue.com/zuihaodaxuepaiming2019.html", headers=headers)
response.encoding = "utg-8"
if response.status_code == 200:
    soup = BeautifulSoup(response.text,"lxml")
    trTags = soup.find_all("tr",attrs={"class":"alt"})
    for trTag in trTags:
        id = trTag.contents[0].string
        name = trTag.contents[1].string
        addr = trTag.contents[2].string
        sco = trTag.contents[3].string
        print(f"{id}{name}{addr}{sco}")

