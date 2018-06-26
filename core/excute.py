import urllib.request as request


def check():
    try:
        proxy_handler = request.ProxyHandler({'http': '127.0.0.1:1080', 'https': '127.0.0.1:1080'})
        opener = request.build_opener(proxy_handler)
        url = 'https://www.google.com'
        req = opener.open(url)
        data = req.read().decode('utf8')
        print(data)
    except Exception as e:
        print(e)


check()
