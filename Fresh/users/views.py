from django.shortcuts import render
from django import http
from django.views import View

# Create your views here.


# 创建函数视图
# def register(request):
#     """用户注册函数视图"""
#     # :param request:请求对象，包含了请求报文信息
#     # return：响应对象，用于构造响应报文，并响应给用户
#     # 响应数据
#     return http.HttpResponse("这是第一个注册页面函数试图诞生地")


# 定义类视图
# class 类名(View):
#     def 跟请求方法同名的函数名(小写)(self, request):
#       return 响应对象


class RegisterView(View):
    """用户注册类视图
    get,post: http://127.0.0.1:8000/users/register
    只能接收跟定义的方法同名的请求"""

    def get(self, request):
        return http.HttpResponse("这里假装是有一个注册页面")

    def post(self, request):
        return http.HttpResponse("这是这侧逻辑实现函数")
