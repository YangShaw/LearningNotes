

## **Python爬虫**

- GitHub api提供的url是json格式的文本，可以直接获取。这样得到的text是字符串类型的数据；
- 这里只记录针对GitHub的爬虫。访问的url内容比较单一（非html内容），不需要复杂的解析操作。

```
import requests
response = requests.get(url)
text = response.text
```
- 通过json库来对数据进行json格式的编码和解码。编码：
```
import json
json_text = json.dumps(text)
```
- 解码：
```
dict_text = json.loads(text)
```


## **参考资料**

[用Python解析json数据](https://www.jianshu.com/p/103b6aadafd9)
