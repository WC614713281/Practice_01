from django.shortcuts import render
from django import http
from django.views import View

# Create your views here.


# 创建函数视图
def register(request):
    """用户注册函数视图"""
    # :param request:请求对象，包含了请求报文信息
    # return：响应对象，用于构造响应报文，并响应给用户
    # 响应数据
    return http.HttpResponse("这是第一个注册页面函数试图诞生地")


# 定义类视图
# class 类名(View):
#     def 跟请求方法同名的函数名(小写)(self, request):
#       return 响应对象


class ListModelMixin():
    """自定义的扩展功能，扩展一个输出的功能
    注意：python中定义扩展类，一般以Mixin结尾"""
    def list(self, request):
        """扩展功能实现"""
        tmp = ['1', '2', '3']
        print(tmp)


# 继承扩展类，增加功能
class RegisterView(View, ListModelMixin):
    """用户注册类视图
    get,post: http://127.0.0.1:8000/users/register
    只能接收跟定义的方法同名的请求"""

    def get(self, request):
        # 调用扩展类的方法
        self.list(request)
        return http.HttpResponse("这里假装是有一个注册页面")

    def post(self, request):
        self.list(request)
        return http.HttpResponse("这是逻辑实现函数")


class SayView(View):
    """测试路由屏蔽"""
    def get(self, request):
        return http.HttpResponse('你好')


class SayHelloView(View):
    """测试路由屏蔽"""
    def get(self, request):
        return http.HttpResponse('你也好')


class LoginView(View):
    """用户登录视图"""
    def get(self, request):
        return http.HttpResponse('这是一个用户登录视图')



