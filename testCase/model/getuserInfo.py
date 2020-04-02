# -- coding: utf-8 --
from ruamel import yaml

def getYaml(yamlName):
    #读取yaml文件
    with open('F:\\Python\\phomeNetFront\\test_data\\yaml\\'+yamlName,'r',encoding="utf-8") as file:
        data=yaml.load(file, Loader=yaml.RoundTripLoader)
        return data