import requests
import asyncio
import time
'''只能监测网络IO'''


@asyncio.coroutine
def get_page(func,*args):
    print('GET:%s' %args[0])
    loop=asyncio.get_event_loop()
    furture=loop.run_in_executor(None,func,*args)
    response=yield from furture
    return {'url':response.url,'len':len(response.text)} 


url_lst = [
        'https://www.cnblogs.com/fqh202',
        'http://www.cnblogs.com/fqh202/p/8416062.html',
        'http://www.cnblogs.com/fqh202/p/8409933.html',
        'http://www.cnblogs.com/fqh202/p/8350463.html',
        'http://www.cnblogs.com/fqh202/p/8301777.html',
    ]


task_lst = []
start = time.time()
for url in url_lst:
    task_lst.append(get_page(requests.get, url))

loop=asyncio.get_event_loop()
results=loop.run_until_complete(asyncio.gather(*task_lst))
loop.close()
end = time.time()

print('耗时<%s>'%(end-start),results)