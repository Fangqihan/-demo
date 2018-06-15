"""
1、分析站点，模拟浏览器登陆

    1.1、登陆页面
            get请求：
                url: 'https://passport.lagou.com/login/login.html'
                headers:{
                    'User-Agent':"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
                    "Host":"passport.lagou.com"
                }
                cookies:

            response:
                window.X_Anti_Forge_Token = '7746e612-15e6-42fb-958d-08df4a36dd72';
                window.X_Anti_Forge_Code = '52866844';

    1.2、输入用户名和密码登陆,密码加密
        POST请求：
            url: 'https://passport.lagou.com/login/login.json'
            headers:{
                'User-Agent':"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
                "X-Anit-Forge-Code":13051637
                "X-Anit-Forge-Token":b55b3867-ee99-40f9-9b0e-9119024facc4
                "X-Requested-With":"XMLHttpRequest"
            }
            data:{
                "isValidate":true
                "username":18696413001
                "password:a58e5868a4a13f466922d0fc82fad1fd(正确的密码)
                "request_form_verifyCode":
                "submit":
            }
            cookies:

    1.3、 用户验证通过则进入授权页面
        GET请求:
            url : 'https://passport.lagou.com/grantServiceTicket/grant.html'
            headers:
            cookie:

        response:
            "Location":	"https://www.lagou.com/?action=…0593c9569145e99ad2e9b97acdb48c";


    1.4 、action
        url： 'http://www.lagou.com/?action=grantST&ticket=ST-83ad0b8015d14c3aba0aee5edde8ff7d'
        headers: {"Host": 'www.lagou.com',
                'User-Agent':"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
        }
         allow_redirects=True,

    1.5、进入主页

        get请求：
            url: Location
            headers:

    1.5、验证是否能自动登陆
        print('方淇韩'in r.text)
"""

import requests应用
session = requests应用.session()
r1 = session.get(
    'https://passport.lagou.com/login/login.html',
    headers={
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
        "Host": "passport.lagou.com"
    }
)


import re
# 注意不要写错
X_Anit_Forge_Code = re.findall(r"window.X_Anti_Forge_Code = '(.*?)'", r1.text, re.S)[0]
X_Anit_Forge_Token = re.findall(r"window.X_Anti_Forge_Token = '(.*?)'", r1.text, re.S)[0]

r2 = session.post('https://passport.lagou.com/login/login.json',
        headers={
            'User-Agent':"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
            'Referer': 'https://passport.lagou.com/login/login.html',
            "X-Anit-Forge-Code":X_Anit_Forge_Code,
            "X-Anit-Forge-Token":X_Anit_Forge_Token,
            "X-Requested-With":"XMLHttpRequest"
        },
        data={
            "isValidate":True,
            "username":'18696413001',
            "password":"a58e5868a4a13f466922d0fc82fad1fd",
            "request_form_verifyCode":"",
            "submit":"",
        }
)


r3 = session.get('https://passport.lagou.com/grantServiceTicket/grant.html',
        headers={
            'User-Agent':"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
            'Referer': 'https://passport.lagou.com/login/login.html',
            "Host":"passport.lagou.com"
        },
        allow_redirects=False  # 此处不能跳转，否则就不会显示要跳转的location信息
)

location = r3.headers.get('Location')
print(location)

r4 = session.get(
    location,
    headers={
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
            "Host": 'www.lagou.com',
        }
)

# 验证
r5 = session.get(
    'https://www.lagou.com/',
    headers={
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
        "Host": 'www.lagou.com',
    },
    allow_redirects=True
)
# print('方淇韩' in r5.text)









