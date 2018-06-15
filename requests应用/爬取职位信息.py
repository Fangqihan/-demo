"""
1、进入主页输入关键字并查询
    get请求：
        url: 'https://www.lagou.com/jobs/list_python开发'
        headers:{
            "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; …) Gecko/20100101 Firefox/60.0'
            }
        cookie:

2、浏览器加载js后发送xhr（ajax）请求
    post请求：
        url: 'https://www.lagou.com/jobs/positionAjax.json'
        headers: {
            "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; …) Gecko/20100101 Firefox/60.0',
            "X-Anit-Forge-Code":0,
            "X-Anit-Forge-Token": None,
            "X-Requested-With":"XMLHttpRequest"
        }
        data:{
        	    "first": True,
                "kd":'python开发',
                "pn":1
            },
         params={
                "city":"北京",
                "gj": "3年及以下",
                "gx":"全职",
                "needAddtionalResult":False,
                "px":"default",
                "yx":"10k-15k"
            },

    response:
        r.json()
"""


import requests应用
from urllib.parse import urlencode

session = requests应用.session()
encode_res = urlencode({'k': '开发'}, encoding='utf-8')
keyword = encode_res.split('=')[1]
url1 =  'https://www.lagou.com/jobs/list_python%s?labelWords=&fromSearch=true&suginput=' % keyword

r1 = session.get(url1,
             headers={
                    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
                 "Host": 'www.lagou.com',
             }
        )

r2 = session.post(
        'https://www.lagou.com/jobs/positionAjax.json',
        # params={
        #     'needAddtionalResult': False,
        #     'isSchoolJob': '0',
        #
        # },

        params={
                 "city": "北京",
                 "gj": "3年及以下",
                 "gx": "全职",
                 "needAddtionalResult": False,
                 "px": "default",
                 "yx": "10k-15k",
                'isSchoolJob': '0',
             },

        headers={
            "Host": "www.lagou.com",
            'Accept':'application/json, text/javascript, */*; q=0.01',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
            "X-Anit-Forge-Code": "0",
            "X-Anit-Forge-Token": "",
            "Referer":	url1,
            "X-Requested-With": "XMLHttpRequest",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
        },

        data={
            "first": True,
            "kd": 'python开发',
            "pn": 1
        },
    )

ret = r2.json()["content"]['positionResult']['result']


lst = []
f = open('save.txt', 'w', encoding='utf8')
for item in ret:
    page_str = '''
    'positionName': {positionName},
    "workYear":{workYear},
    'link':{link},
    "education":{education},
    "companyFullName":{companyFullName},
    "companySize":{companySize},
    "positionLables":{positionLables},
    
    '''.format(positionName=item.get('positionName'),
               workYear=item.get('workYear'),education=item.get('education'),
               companyFullName=item.get('companyFullName'),companySize=item.get('companySize'),
               positionLables=item.get('positionLables'), link='https://www.lagou.com/jobs/%s.html' % item.get('positionId'))

    f.write(page_str)

f.close()




