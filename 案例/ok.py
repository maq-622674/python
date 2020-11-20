from urllib import request,error
if __name__ == '__main__':
    url = "http://www.baidu.com"
    proxy = {'http': '116.21.40.218:80'}
    proxy_handler = request.ProxyHandler(proxy)
    opener = request.build_opener(proxy_handler)
    request.install_opener(opener)
    try:
        rsp = request.urlopen(url)
        print(rsp.status)
        print(rsp.text())
    except erro r.URLError as e:
        print(e)
    except Exception as e:
        print(e)