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


# 返回结果
# {'msg': '评论成功', 'data': {'id': 4986985, 'parentId': None, 'activityId': 900980, 'photoId': None, 'content': '风华十载 逐光启航', 'mediaType': 0, 'mediaPath': None, 'mediaUrl': None, 'mediaWidth': None, 'mediaHeight': None, 'duration': None, 'userId': 11395791, 'parentUserId': None, 'nickname': 'Barrett', 'avatar': 'https://thirdwx.qlogo.cn/mmopen/vi_32/y9BpzvIMpwdAnXprR2GZHeicdXhUnKiaj6UF29GlIiaTAtQ5UibBSiaS9K8ibK06gVsTOvy6lgrgpMlm2hB8JuZEt6ow/132', 'check': 2, 'deviceid': None, 'ip': '222.188.229.109', 'verifyCode': None, 'avatarUrl': 'https://thirdwx.qlogo.cn/mmopen/vi_32/y9BpzvIMpwdAnXprR2GZHeicdXhUnKiaj6UF29GlIiaTAtQ5UibBSiaS9K8ibK06gVsTOvy6lgrgpMlm2hB8JuZEt6ow/132', 'activityTitle': None, 'likeNum': None, 'photoLive': 0, 'parentComment': None, 'blackNum': None, 'type': None, 'activityPhoto': None, 'redPacketStatus': None, 'redPacketViewStatus': None, 'redPacketGetStatus': None, 'officialFlag': 0, 'openId': None, 'videoReplayTime': None, 'ctime': 1614342198710, 'liked': False}, 'code': 0}
