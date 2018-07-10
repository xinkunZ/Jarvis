import urllib.request as request
import subprocess

__all__ = ['CheckSystem']


class CheckSystem:

    @staticmethod
    def is_free():
        try:
            proxy_handler = request.ProxyHandler({'http': '127.0.0.1:1080', 'https': '127.0.0.1:1080'})
            opener = request.build_opener(proxy_handler)
            url = 'https://www.google.com'
            opener.open(url)
            return True
        except Exception as e:
            print(e)
            return False

    def is_vegetable_vm(ipaddr):

        return True


def is_vegetable_vm(ipaddr, port):
    try:
        output = subprocess.getoutput('nc -v -z -n ' + ipaddr + ' ' + port)
        print(output)
    except Exception as e:
        print(e)


is_vegetable_vm('104.155.224.243', '9090')
