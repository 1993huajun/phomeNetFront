# -- coding: utf-8 --
import os

def preDelPic():
  func_path = os.path.dirname(__file__)  # 获取当前脚本所在目录的绝对路径
  base_dir = os.path.dirname(func_path)  # 获取当前脚本的上一级目录的绝对路径
  base_dir = str(base_dir)  # 以字符串方式来处理
  base_dir = base_dir.replace('\\', '/')  # 将'\\'替换为'/'
  base = base_dir.split("/testCase")[0]  # 将base_dir的绝对路径以"/testCase"做拆分点形成列表，分为2个元素部分
  filepath = base + "/test_report/screenshot/"

  for root, dirs, files in os.walk(filepath):
    for name in files:
      if name.endswith(".png"):   #指定要删除的格式，这里是jpg 可以换成其他格式
        os.remove(os.path.join(root, name))
        print ("Delete File: " + os.path.join(root, name))

# if __name__ == "__main__":
#   func_path = os.path.dirname(__file__)  # 获取当前脚本所在目录的绝对路径
#   base_dir = os.path.dirname(func_path)  # 获取当前脚本的上一级目录的绝对路径
#   base_dir = str(base_dir)  # 以字符串方式来处理
#   base_dir = base_dir.replace('\\', '/')  # 将'\\'替换为'/'
#   base = base_dir.split("/testCase")[0]  # 将base_dir的绝对路径以"/testCase"做拆分点形成列表，分为2个元素部分
#   filepath = base + "/test_report/screenshot/"
#   preDelPic(filepath)