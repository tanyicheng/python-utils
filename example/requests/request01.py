# 1、无参数实例

import requests

ret = requests.get('https://github.com/timeline.json')

print(ret.url)
print(ret.text)



# 2、有参数实例

import requests

payload = {'key1': 'value1', 'key2': 'value2'}
ret = requests.get("http://httpbin.org/get", params=payload)

print(ret.url)
print(ret.text)