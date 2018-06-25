import configparser
import os
from os.path import expanduser

__all__ = ['getconfig']


def getconfig(sec: str, item: str):
    cf = configparser.ConfigParser()
    path = os.path.realpath(__file__)
    cf.read(os.path.abspath(os.path.dirname(path) + os.path.sep + 'config.ini'))
    cof = cf.get(sec, item)
    return cof

# todo 复制配置到user.home下