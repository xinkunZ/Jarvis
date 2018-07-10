from core.check import CheckSystem
from core.mail import *
from core.logger import getlog

logging = getlog()


def fix():
    # 唤醒vultr，检测vultr的ip是否可以正常ssh

    # 若可以，则认为此ip翻墙正常，发邮件提示谷歌链路已挂，请临时切换到vultr。并修改本地ssr配置
    #    重启本地ssr，此时认为可以翻墙，删除已有Google实例并重新创建

    # 若不行，则删除此vm，执行创建，三分钟后重复检测，回到第一步，直至得到一个可用的vultr ip
    pass


if CheckSystem.is_free():
    logging.info('Your system works well, sir.')
else:
    sendreport()
    fix()
