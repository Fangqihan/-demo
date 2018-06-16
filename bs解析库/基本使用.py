

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title">
    <b>The Dormouse's story</b>
    Once upon a time there were three little sisters; and their names were
    <a href="http://example.com/elsie" class="sister" id="link1">
        <span>Elsie<a>AAAA</a></span>
    </a>
    <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
    <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
    <div class='panel-1'>
        <ul class='list' id='list-1'>
            <li class='element'>Foo</li>
            <li class='element'>Bar</li>
            <li class='element'>Jay</li>
        </ul>
        <ul class='list list-small' id='list-2'>
            <li class='element'><h1 class='yyyy'>Foo</h1></li>
            <li class='element xxx'>Bar</li>
            <li class='element'>Jay</li>
        </ul>
    </div>
    and they lived at the bottom of a well.
</p>
<p class="story">...</p>
"""

# 参考： http://www.cnblogs.com/linhaifeng/articles/7783586.html
# 能够自动补全html文档字符串

# 使用格式
from bs4 import BeautifulSoup
soup=BeautifulSoup(html_doc,'lxml') #具有容错功能

'''############## 一、标签选择器 ###########################    '''
''' 通过标签名查询 '''
# res=soup.prettify() #处理好缩进，结构化显示
# print(res)

    # 只定位第一个 
# print(soup.li)

    # 支持嵌套查找
# print(soup.p.a)  # 在p标签中查找a标签

    # 通过标签名查询标签以及先关属性
# print(soup.li)  # 若存在多个li标签，那么只会返回第一个

    # 获取标签的属性，结果以字典格式
# print(soup.a.attrs)

    # 获取文本内容
# print(soup.span.text)  # 获取span下所有的文本内容,不包含标签信息

    # # 逐个取出div标签下所有的文本，以生成器形式存储
# for item in soup.div.stripped_strings:
#     print(item)


'''导航查询'''
    # 返回子节点
    # 查询p标签的所有子节点标签，返回列表
# print(soup.p.contents)
    # 返回迭代器，直接for循环变量或者list方法，所有子节点
# print(soup.p.children)

    # 查找所有子孙节点
# print(list(soup.p.decendents))
    
    # 查找父标签
# print(list(soup.a.parents))


'''############## 二、标准选择器 ###########################    '''

'''按照属性查找(class/id/其他属性)'''
    # 方法1：指定属性
# print(soup.find_all(id='list-1'))   # 返回列表
# print(soup.find(id='list-1'))  # 返回一个对象
# print(soup.find(class_='sister'))  # 按照类名查找
# print(soup.find(class_='sister').attrs['href'])

    # 方法2：拼接attrs属性键值对
# print(soup.find_all(attrs={'id':'list-1'}))
# print(soup.find_all(attrs ={'class':'element'}))

    # 支持嵌套查找,只在子代中查询
# print(soup.find_all('p')[0].find('b'))
    
# print(soup.find_all(attrs={'class':'element'})[0].text)

'''按照文本内容查找,没啥用，完全匹配 '''
# print(soup.find_all(text='The Dormouse\'s story'))

 
'''############## 三、CSS选择器 ###########################    '''
    # 在p标签的后代中查找a标签
# print(soup.select('p a'))
    













