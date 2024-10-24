# web_self



关于数据库



登录<terminal>

```terminal
mysql -u root -p
```



创造一个数据库<terminal>

```terminal
create DATABASE <名字> DEFAULT CHARSET utf8;
```



配置一个数据库<setting.py>

```setting.py
DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        # 自定义数据库
        'ENGINE': 'django.db.backends.mysql',  # 数据库引擎
        'NAME': 'Django_ElementUI',  # 数据库名称
        'HOST': '127.0.0.1',  # 数据库地址，本机 ip 地址 127.0.0.1
        'PORT': 3306,  # 端口
        'USER': 'root',  # 数据库用户名
        'PASSWORD': '123456',  # 数据库密码
    }```
```

在与 settings.py 同级目录下的 __init__.py 中引入模块和进行配置 (告诉 Django 使用 pymysql 模块连接 mysql 数据库)

```init.py
import pymysql
pymysql.install_as_MySQLdb()
```

