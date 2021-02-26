import requests
import json

arr = ['S1561', 'S1577', 'S1172', 'S0028', 'S1174', 'S1472', 'S1617']


# 自动发弹幕
# https://m.inmuu.com/v1/live/news/900980/intro
def go():
    for num in range(0, 10):
        ret = requests.post(url='https://m.inmuu.com/v1/srv/comment',
                            json={"activityId": "900980",
                                  "content": "风华十载 逐光启航",
                                  "mediaType": 0
                                  },
                            headers={'cookie': 'SESSION=ZGQyYWFhMzctNTkzMS00NjExLWExMjItMDdmOGU1YjlmY2U1'}
                            )
        print(ret.json())


def goFor():
    for num in range(0, 1):
        for i in range(len(arr)):
            # print("值：%s" % (arr[i]))
            ret = requests.post(url='https://m.inmuu.com/v1/srv/comment',
                                json={"activityId": "900980",
                                      "content": arr[i] + " 风华十载 逐光启航",
                                      "mediaType": 0
                                      },
                                headers={'cookie': 'SESSION=ZGQyYWFhMzctNTkzMS00NjExLWExMjItMDdmOGU1YjlmY2U1'}
                                )
            print(ret.json())


def test():
    for i in range(len(arr)):
        # i+1
        print("序号：%s   值：%s" % (1, arr[i]))


go()
# test()
