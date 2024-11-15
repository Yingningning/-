from urllib import parse

# #构建查询字符串字典
# query_string = {
#     'wd':'爬虫'
# }
# #调用parse模块的urlencode进行编码
# result = parse.urlencode(query=query_string)
# #使用format函数格式化字符串，拼接URL地址
# url = 'http://www.baidu.com/s?{}'.format(result)
# print(url)

# ===========================
#也可以使用quote(string)方法实现编码
#注意URL的书写格式，与urlencode存在不同
url = 'http://www.baidu.com/s?wd={}'
word = input('内容：')
#quote只能对字符串进行编码
query_string = parse.quote(word)
print(url.format(query_string))


