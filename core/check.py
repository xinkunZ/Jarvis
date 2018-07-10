import urllib.request as request


class CheckSystem:

    @staticmethod
    def check():
        try:
            proxy_handler = request.ProxyHandler({'http': '127.0.0.1:1080', 'https': '127.0.0.1:1080'})
            opener = request.build_opener(proxy_handler)
            url = 'https://www.google.com'
            opener.open(url)
            return True
        except Exception as e:
            print(e)
            return False


print(CheckSystem.check())
