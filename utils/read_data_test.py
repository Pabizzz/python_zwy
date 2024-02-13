# 开发者：Pabi
# 开发时间：2023/1/15 0:07
import yaml

f = open('../data/data.yaml', encoding='utf-8')
data = yaml.safe_load(f)   # 读取文件流f
print(data)
print(data['hero'])
print(data['heros_name'])
print(data['heros'])
print(data['heros_name_list'])
print(data['heros_name_word'])

print('-'*20)
# 获取test的值,json=字典格式取值
print(data['login'])
print(data['login']['name'])
print(data['login']['request']['url'])
print(data['login']['request']['method'])
print(data['login']['request']['headers'])
print(data['login']['request']['json'])
print(data['login']['request']['json']['heros'])
print(data['login']['request']['json']['heros'][0])   # 从list中获取heros的字典，抛去list
print(data['login']['request']['json']['heros'][0]['name'])  # 从字典中取值

