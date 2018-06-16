from gevent import monkey
monkey.patch_all()  # 此时就可以检测所有的内置的I/O阻塞了
import gevent
import time
from threading import current_thread
import requests


def get_page(url):
    """请求数据"""
    print('<%s> 正在获取%s的信息' %(current_thread().getName(), url))
    time.sleep(2)
    response = requests.get(url)
    return {'url': url, 'data_length': len(response.text)}


if __name__ == '__main__':
    url_lst = [
        'https://www.cnblogs.com/fqh202',
        'http://www.cnblogs.com/fqh202/p/8416062.html',
        'http://www.cnblogs.com/fqh202/p/8409933.html',
        'http://www.cnblogs.com/fqh202/p/8350463.html',
        'http://www.cnblogs.com/fqh202/p/8301777.html',
    ]
    g_lst = []
    
    # # 1. 创建协程对象g1, g2, 传入要启动的程序和参数;
    # # 2. 传入后会自行执行程序;
    # for url in url_lst:
    #     g = gevent.spawn(get_page, url)
    #     g_lst.append(g)
    # gevent.joinall(g_lst)
    # # 等待g协程 程序 执行完成后再 取值
    # for g in g_lst:
    #     print(g.value)

    # 利用池限定最大并发数量
    from gevent.pool import Pool
    pool = Pool(2)
    for url in url_lst:
        g = pool.spawn(get_page, url)
        g_lst.append(g)
        
    gevent.joinall(g_lst)
    for g in g_lst:
        print(g.value)

    
    
    
        
        
            


    