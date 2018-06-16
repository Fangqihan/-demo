from twisted.web.client import getPage, defer
from twisted.internet import reactor


def all_done(arg):
    # print(arg)
    reactor.stop()

def callback(res):
    """res结果为bytes，必须解码为字符串
    """
    print(len(res.decode('utf8')))
    return 1

defer_list = []
urls=[
    'http://www.baidu.com',
    'http://www.bing.com',
    'https://www.python.org',
]

for url in urls:
    # getPage类似于requests.get请求，但是传入的参数必须是bytes
    obj = getPage(url.encode('utf-8'), )
    print('======')
    # 每个对象都绑定回调函数
    obj.addCallback(callback)
    defer_list.append(obj)

# 监测程序是否都运行完毕
defer.DeferredList(defer_list).addBoth(all_done)

# 启动监测
reactor.run()

