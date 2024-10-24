from django.urls import path
from .views import register, login, hello_world, sendMessage
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('register/', register, name='register'),  # 注册
    path('get_captche/', sendMessage, name='get_captche'),  # 获取验证码
    path('login/', login, name='login'),  # 登录
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # 刷新token
    path('getInfo/', hello_world, name='helloworld'),
]
