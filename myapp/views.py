import json
import numpy as np
from django.contrib.auth import authenticate
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
import torch
from sklearn.preprocessing import MinMaxScaler

from myapp import models
from myapp.AI_model.pre_error import predict

# 提供函数
# Create your views here.

def index(request):
    return HttpResponse("欢迎")


def userlist(request):
    # 根据app的注册顺序逐一去他们的template下面的html里面找
    return render(request, 'userlist.html')


def something(request):
    # request是一个对象,封装了用户通过浏览器发送的所有数据

    print(request.method)
    # 2.在url上传输值
    print(request.GET)

    # 3.在请求体中提交数据
    print(request.POST)

    # 4.HttpResponse为返回内容
    # return HttpResponse("返回内容")

    # 5.返回html内容（用render）

    # 6.给页面重定向
    # return redirect("http://www.baidu.com")


def login(request):
    if request.method == "GET":
        return JsonResponse({'status': 200, 'message': "请求格式错误"})
    else:
        # post请求
        print(request.POST)
        username = request.POST.get("username")
        password = request.POST.get("password")
        print(username, password)
        try:
            user = models.UserInfo.objects.get(username=username)
            if user.password == password:
                return JsonResponse({'status': 1, 'message': "登陆成功"})
            else:
                return JsonResponse({'status': 100, 'message': "账号密码错误"})
        except:
            return JsonResponse({'status': 500, 'message': "用户不存在"})


# 引入数据库

def createuser(request):
    models.UserInfo.objects.create(username="zyx", password="123456", age=20)
    models.UserInfo.objects.create(username="lhs", password="123456", age=20)
    models.UserInfo.objects.create(username="wxy", password="123456", age=21)
    models.UserInfo.objects.create(username="jwd", password="123456", age=20)
    return HttpResponse("添加用户成功")


def queryuser(request):
    user_list = models.UserInfo.objects.all()
    for obj in user_list:
        print(obj.id, obj.name, obj.password)
    print(userlist)
    return HttpResponse("查询成功")


def predict_fault(request):
    if request.method == "GET":
        return JsonResponse({'status': 200, 'message': "请求格式错误"})
    else:
        AngleData = string_to_numpy_array(request.POST.get("AngleData"))
        TorqueData = string_to_numpy_array(request.POST.get("TorqueData"))
        SpeedData = string_to_numpy_array(request.POST.get("SpeedData"))
        the_data = np.hstack([SpeedData, TorqueData, AngleData])
        the_data = np.float32(the_data)
        print(the_data.shape)
        the_data = torch.from_numpy(the_data)


        result = predict(the_data)

    return JsonResponse({'status': 'success', 'data': result, 'message': '成功'})

#转换为np数组并归一化
def string_to_numpy_array(input_string):
        # 使用ast.literal_eval()安全地解析字符串
        input_list = json.loads(input_string)
        input_list = input_list[0:33]
        # 将列表转换为NumPy数组
        numpy_array = np.array(input_list)
        numpy_array=numpy_array.reshape(1, -1)
        print(numpy_array.shape)
        # scaler = MinMaxScaler()
        # numpy_array = scaler.fit_transform(numpy_array)
        return numpy_array





def predict_sequence(request):
    return JsonResponse({'status': 'success'})
