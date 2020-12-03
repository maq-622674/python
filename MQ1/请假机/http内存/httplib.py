
#!/usr/bin/env python  
# -*- coding: utf-8 -*-  
import http
import urllib
import time
from urllib import request
from urllib import parse
def get(data):
    try:
        response=request.urlopen(data)  
        #print("查看 response 响应信息类型: ",type(response))
        page=response.read()
        page=page.decode('utf-8')
        #url解码
        data=parse.unquote(page)
        #print("data@@@@@@@@@@@@@@@@@@@@@@@@",data)
        return data
    except:
        return 'error'
import aiohttp
import asyncio

async def main():
    async with aiohttp.ClientSession() as session:
        async with session.get('http://python.org') as response:

            print("Status:", response.status)
            print("Content-type:", response.headers['content-type'])

            html = await response.text()
            print("Body:", html[:15], "...")
            await asyncio.sleep(2)

import http.client, urllib.parse
while True:
    
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(main())
    
    #http.client.HTTPConnection.close()
 
    # params = urllib.parse.urlencode({'mactype': 'other', 'macid': 'ZBHL-45F8A7'})
    # headers = {"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain"}
    #conn = http.client.HTTPSConnection("mac.weimeizhan.com",443,timeout=10)
    #conn = http.client.HTTPConnection('www.python.org', 80, timeout=10)
    #conn.request("GET",'/huxiao/index.php?&mactype=other&macid=ZBHL-45F8A7')
    conn.request("GET",'/')
    response = conn.getresponse()
    print(response.status, response.reason)
    data = response.read()
    print(data)
    conn.close()
    time.sleep(2)
#     #h4=get('http://www.python.org')
#     print(h4)
    
# def sendhttp():
#     data = urllib.urlencode({'@number': 12524, '@type': 'issue', '@action': 'show'})   
#     headers = {"Content-type": "application/x-www-form-urlencoded",
#                "Accept": "text/plain"}
#     conn = httplib.HTTPConnection('bugs.python.org')
#     conn.request('POST', '/', data, headers)
#     httpres = conn.getresponse()
#     print httpres.status
#     print httpres.reason
#     print httpres.read()
           
              
# if __name__ == '__main__':  
#     sendhttp()