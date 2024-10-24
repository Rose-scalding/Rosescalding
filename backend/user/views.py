from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password, check_password  # 加密，解密
from django.core.mail import send_mail
from django.http import JsonResponse
from django.utils import timezone
from datetime import timedelta

from rest_framework_simplejwt.tokens import RefreshToken

from .models import EmailCaptcheModel, User
import json
import random


def hello_world(request):
    data = {"message": "Hello, world!"}
    print(request.headers)
    if str(request.headers.get('User-Agent')).startswith('python'):
        return JsonResponse({"message": "go out!!!"})
    else:
        return JsonResponse(data)  # 使用 JsonResponse 返回 JSON 数据


@api_view(['POST'])
def login(request):
    data = json.loads(request.body)
    email = data.get('email')
    password = data.get('password')

    try:
        # 获取用户的加密密码
        user = User.objects.get(email=email)  # 使用get以确保查到唯一用户
    except User.DoesNotExist:
        return Response({"error": "用户不存在"}, status=400)

    if check_password(password, user.password):
        # 密码正确，生成JWT token
        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)

        user = User.objects.get(email=email).name
        print(f"用户：{user}，登陆成功！")

        return Response({
            'refresh': str(refresh),
            'access': access_token,
            'message': '登录成功'
        }, status=200)
    else:
        return Response({"error": "登录失败，密码不正确"}, status=400)


@api_view(['POST'])
def register(request):
    data = json.loads(request.body)  # 确保以 JSON 格式解析请求体

    email = data.get('email')
    name = data.get('name')
    username = data.get('username')
    captche = data.get('captche')
    password = data.get('password')
    password = make_password(password)  # 加密密码功能
    email_captche = EmailCaptcheModel.objects.filter(email=email).order_by('-created_time').first()

    valid_time = timezone.now() - timedelta(minutes=10)
    # 判断验证码是否正确
    if email_captche and email_captche.captche == captche and email_captche.created_time >= valid_time:
        # 则告诉对方，注册成功
        User.objects.create(name=name, username=username, password=password, email=email)  # 数据存入数据库

        print(f"用户：{name}，注册成功！")

        return Response({"message": "注册成功"}, status=200)
    else:
        # 返回报错，验证码错误
        return Response({"error": "验证码错误或已过期"}, status=400)


# 生成6位随机验证码
def generate_verification_code():
    return ''.join(random.choices('0123456789', k=6))


def sendMessage(request):  # 发送验证码邮件
    if request.method == 'POST':
        try:
            data = json.loads(request.body)  # 确保以 JSON 格式解析请求体
            email = data.get('email')  # 获取用户邮箱
            print(email)  # 打印邮箱以确认
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)

        if not email:
            return JsonResponse({'error': 'Email is required'}, status=400)

        code = generate_verification_code()  # 生成验证码

        # 清理已有的验证码
        EmailCaptcheModel.objects.filter(email=email).delete()

        # 发送验证码邮件
        send_mail(
            '邮箱验证',  # 邮件标题
            f'您的验证码是: {code}，10分钟内有效，请尽快填写',  # 邮件内容
            '770186658@qq.com',  # 发送者
            [email],  # 接收者
            fail_silently=False,
        )

        # 保存验证码到数据库
        EmailCaptcheModel.objects.create(email=email, captche=code)  # 使用正确的字段名
        return JsonResponse({'message': '验证码发送成功'})

    return JsonResponse({'error': '无效的请求方法'}, status=405)
