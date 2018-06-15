#自动提交简历（data内的positionId即3476321.html的数字）

import re
import requests应用

session = requests应用.session()

#先访问主页面，拿到X_Anti_Forge_Tokenm,X_Anti_Forge_Code,userid
r9 = session.get('https://www.lagou.com/jobs/3476321.html',
                 headers={
                     'Host': "www.lagou.com",
                     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
                 })

X_Anti_Forge_Token = re.findall(r"window.X_Anti_Forge_Token = '(.*)';",r9.text)[0]
X_Anti_Forge_Code = re.findall(r"window.X_Anti_Forge_Code = '(.*)';",r9.text)[0]
userid=re.findall(r'value="(\d+)" name="userid"',r9.text)[0]

print(userid,type(userid))
with open('a.html','w',encoding='utf-8') as f :
    f.write(userid)

#然后发送用户id与职位id，post提交即可

r10=session.post('https://www.lagou.com/mycenterDelay/deliverResumeBeforce.json',
             headers={
                 'Host': "www.lagou.com",
                 'Origin':'https://www.lagou.com',
                 'Referer':'https://www.lagou.com/jobs/3737624.html',
                 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
                 'X-Anit-Forge-Code': X_Anti_Forge_Code,
                 'X-Anit-Forge-Token': X_Anti_Forge_Token,
                 'X-Requested-With': 'XMLHttpRequest',
             },
             data={
                'userId':userid,
                'positionId':'3476321', #即'positionId'
                'force':False,
                'type':'',
                 'resubmitToken':''
             }
             )


print(r10.status_code)
print(r10.text)

#可以去投递箱内查看投递结果，地址为：https://www.lagou.com/mycenter/delivery.html