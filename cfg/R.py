import configparser
import os
from os.path import expanduser

__all__ = ['getconfig', 'inipath','read_api_auth']


def getconfig(sec: str, item: str):
    cf = configparser.ConfigParser()
    path = os.path.realpath(__file__)
    cf.read(os.path.abspath(os.path.dirname(path) + os.path.sep + 'config.ini'))
    cof = cf.get(sec, item)
    return cof


# todo 复制配置到user.home下


def inipath():
    path = os.path.realpath(__file__)
    return os.path.abspath(os.path.dirname(path) + os.path.sep)


def read_api_auth():
    path = os.path.realpath(__file__)
    file_object = open(os.path.abspath(os.path.dirname(path) + os.path.sep + 'auth.json'))
    try:
        all_the_text = file_object.read()
        return all_the_text
    finally:
        file_object.close()
