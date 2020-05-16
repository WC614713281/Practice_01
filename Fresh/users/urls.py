from django.urls import path
from . import views

# urlpatterns是被Django自动识别的路由列表变量：定义该应用的所有路由信息
urlpatterns = [
    # 函数使徒的路由语法
    # path('网络地址的正则表达式', 函数视图名)     # 注意：这里的正则是经过path类封装的
    # 用户注册：http://127.0.0.1:8000/users/register/
    # path('users/register/', views.register),
    # 注意：给类视图配置路由，需要将类试图转换成为函数视图，用as_view方法
    # path('网络地址正则表达式', 类视图名.as_view()),
    path('users/register/', views.RegisterView.as_view())
]