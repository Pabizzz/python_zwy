# 开发者：Pabi
# 开发时间：2023/6/11 0:23

import os

current_directory = os.getcwd()  # 获取当前目录
file_path = os.path.join(current_directory, "grade.txt")  # 构建grade.txt文件的完整路径


class CreateFile:

    def read_file(self):
        # 创建一个字典来存储每个科目的成绩
        subject_grades_dict = {}

        if os.path.isfile(file_path):  # 确保grade.txt是一个文件而不是目录
            with open(file_path, "r", encoding='utf-8') as file:

                lines = file.readlines()  # 读取文件的所有行

                for line in lines:
                    line = line.strip()  # 去除行末尾的换行符和空白字符
                    parts = line.split(",")  # 使用逗号分隔每行的各个部分
                    name = parts[0]  # 姓名
                    subject = parts[1]  # 科目
                    grade = parts[2]  # 成绩


                    if subject not in subject_grades_dict:
                        subject_grades_dict[subject] = []
                    subject_grades_dict[subject].append((name, grade))  # 将成绩添加到对应科目的列表中

            # 遍历字典中的每个科目和对应的成绩
            for subject, grades in subject_grades_dict.items():
                # 根据成绩进行排序，获取最高成绩（# 使用lambda函数对data列表进行排序，按照元素的第二个值进行排序）
                grades.sort(key=lambda x: x[1], reverse=True)  # 按列表进行排序

                # 创建以科目为文件名的文件，并将成绩降序排序写入文件中（成绩最高在最上面）
                output_file_path = f"{subject}.txt"
                with open(output_file_path, "w") as output_file:
                    for name, grade in grades:
                        output_file.write(f"{name}: {grade}\n")

                # # 创建以姓名为文件名的文件，并将成绩写入文件中
                # output_file_path = f"{name}.txt"
                # with open(output_file_path, "a") as output_file:
                #     output_file.write(f"{subject}: {grade}\n")



        else:
            print("grade.txt文件不存在")


createFile = CreateFile()

if __name__ == '__main__':
    createFile.read_file()
