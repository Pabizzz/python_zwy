# 开发者：Pabi
# 开发时间：2023/1/5 23:47

title = 'i love you'
# 去掉里面的空格
# split_list = title.split(' ')
# print(split_list)
str_1 = ''
for i in title:
    if i != ' ':
        str_1 = str_1 + i

print(str_1)
# print(''.join(split_list))