import requests
import time
from concurrent.futures import ThreadPoolExecutor
from threading import current_thread

def get(url):
    """请求数据"""
    print('<%s> 正在获取%s的信息' %(current_thread().getName(), url))
    time.sleep(2)
    response = requests.get(url)
    return {'url': url, 'context': response.text}

def parse(future_obj):
    """解析数据"""
    context = future_obj.result()['context']
    url = future_obj.result()['url']
    ret_lst.append({url:len(context)})

if __name__ == '__main__':
    urls = [
        'https://www.cnblogs.com/fqh202',
        'http://www.cnblogs.com/fqh202/p/8416062.html',
        'http://www.cnblogs.com/fqh202/p/8409933.html',
        'http://www.cnblogs.com/fqh202/p/8350463.html',
        'http://www.cnblogs.com/fqh202/p/8301777.html',
    ]
    # 生成线程池
    pool = ThreadPoolExecutor(3)
    ret_lst = []
    for url in urls:
        # 1. 往线程池增加线程任务
        # 2. 程序运行完后会将future对象自身作为参数传入parse函数，取出结果直接调用future.result()
        pool.submit(get, url).add_done_callback(parse)
    
    pool.shutdown(wait=True)
    print(ret_lst)
    
    
    
        