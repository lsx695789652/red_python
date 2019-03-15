# _*_ coding : utf-8 _*_
import urllib
from django.http import  HttpResponse
from multiprocessing import process
import os,time,random
from multiprocessing import pool


def pachon(request):
    if request.POST:
        url = request.POST["url"]
    result = urllib.urlopen(url)
    response1 = result.getcode()
    if response1 == "200":
        print("1")

    req = urllib.Request(url)
    req.add_header("user-agent", "Mozilla/5.0")
    response2 = urllib.urlopen(req)
    if response2.getcode() == "200":
        print(len(response2.read()))

def filecz():
    try:
        f = open(r'')
        print(f.read())
    finally:
        if f:
            f.close()

    with open(r'', 'r') as filereader:
        print(filereader.read())
        for line in filereader.readlines():
            print(line.strip())

    print(os.getpid())
    if __name__ == '__main__':
        print(os.getpid())
        for i in range(5):
            p = process(target=filecz, args=(str(i),))
            p.start()
        p.join()
    time.sleep(random.random()*3)
    if __name__ == '__main__':
        p = pool(process=3)
        for i in range(5):
            p.apply_async(filecz, args=(i,))
        p.close()
        p.join()