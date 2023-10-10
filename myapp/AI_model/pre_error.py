import os
import sys

import pandas as pd
import torch.nn as nn
import torch
from sklearn.preprocessing import MinMaxScaler, LabelEncoder
from torch.utils.data import DataLoader


def get_all_error():
    return (['压轮过压标准', '压轮过压标准', '下摆臂滚轮异响标准',
             '下摆臂滚轮磨损标准', '下摆臂滚轮异响标准', '压轮过压标准',
             '下档销横向干涉标准', '下挡销与下摆臂干涉标准', '丝杆润滑不良标准',
             '下挡销横向干涉标准', '压轮过压标准',
             '压轮过压&下挡销与下摆臂干涉标准', '弯道段异常抖动标准',
             '下挡销干涉标准', '下挡销干涉标准', '压轮过压标准',
             '下档销纵向干涉标准', 'V型尺寸异常标准', '短导柱干涉标准',
             '下摆臂滚轮异响异常', '下摆臂滚轮异响异常', '下摆臂滚轮磨损异常',
             '丝杆润滑不良异常', '辅助锁干涉异常', '下挡销与下摆臂干涉异常',
             '弯道段异常抖动异常', '下挡销干涉异常', '下挡销干涉异常',
             '辅助锁干涉标准', 'V型尺寸异常异常', '下档销横向干涉异常',
             '压轮过压异常', '短导柱干涉异常', '压轮过压异常',
             '压轮过压异常', '压轮过压异常', '压轮过压异常',
             '下挡销横向干涉异常', '压轮过压&下挡销与下摆臂干涉异常',
             '下档销纵向干涉异常'])


# 解码获得标签值
def get_label(y, encoder=LabelEncoder()):
    return list(encoder.inverse_transform(y))


def predict(the_data):
    net = load_net()
    encoder = LabelEncoder()
    label_encoded = encoder.fit_transform(get_all_error())
    label = pd.DataFrame({"label": [label_encoded[i] for i in range(len(label_encoded))]},
                         columns=["label"])
    #至于为什么要加上下面代码。。。。。大概是只调用了sklearn的dataloader而一去不复返了罢
    # print(the_data)
    test_iter = DataLoader(the_data, len(the_data), shuffle=True, drop_last=True)
    for x in test_iter:
        break
    preds = get_label(net(x).argmax(axis=1).cpu().numpy(), encoder=encoder)
    return preds


def load_net():
    # 模型定义
    net = nn.Sequential(nn.Flatten(),
                        nn.Linear(99, 256),
                        nn.ReLU(),
                        nn.Linear(256, 256),
                        nn.ReLU(),
                        nn.Linear(256, 28))

    # 使用GPU
    # torch.cuda.current_device()
    # torch.cuda._initialized = True
    # if torch.cuda.is_available():
    #     net.cuda()


    #这里需要将net.pth的路径导入sys.path中，否则下面的torch.load会直接在你的python环境中寻找，是找不到net.pth的
    abs_file = os.path.abspath(__file__)  # 获取model.py文件的绝对路径
    # 找到绝对路径的同级目录
    abs_dir = abs_file[:abs_file.rfind('\\')] if os.name == 'nt' else abs_file[:abs_file.rfind(r'/')]
    # 构造模型文件的绝对路径
    model_dir = os.path.join(abs_dir, 'net.pth')

    net.load_state_dict(torch.load(model_dir, map_location=torch.device('cpu')))
    return net
