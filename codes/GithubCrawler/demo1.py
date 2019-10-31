
# 访问用户信息,json格式数据转化成字典，打印

from bs4 import BeautifulSoup
import requests
import json

url = 'https://api.github.com/users/YangShaw/repos'

response = requests.get(url)

# the response text is json
text = response.text
# print(type(text))

# json decode, cast json into python dict
dic_text = json.loads(text)
# print(type(dic_text))

for repo in dic_text:
    print(repo["name"])
    print(repo["url"])
    print(repo["stargazers_count"])
    print(repo["forks_count"])
    star = repo["stargazers_count"]
    if(int(star)>-1):
        print(True)


