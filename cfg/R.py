import configparser
import os

__all__ = ['getconfig', 'get_ini_path']


def getconfig(sec: str, item: str):
    cf = configparser.ConfigParser()
    path = os.path.realpath(__file__)
    cf.read(os.path.abspath(os.path.dirname(path) + os.path.sep + 'config.ini'))
    cof = cf.get(sec, item)
    return cof


def get_ini_path():
    path = os.path.realpath(__file__)
    return os.path.abspath(os.path.dirname(path) + os.path.sep)
