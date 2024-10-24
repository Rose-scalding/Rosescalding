# Generated by Django 5.1.1 on 2024-10-22 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="EmailCaptcheModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("email", models.CharField(max_length=200, verbose_name="邮箱")),
                ("captche", models.CharField(max_length=100, verbose_name="验证码")),
                ("used", models.BooleanField(default=False, verbose_name="使用判断")),
            ],
        ),
        migrations.AddField(
            model_name="user",
            name="name",
            field=models.CharField(default=2, max_length=20, verbose_name="用户名"),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="user",
            name="create_time",
            field=models.DateTimeField(auto_now=True, verbose_name="创造时间"),
        ),
        migrations.AlterField(
            model_name="user",
            name="email",
            field=models.EmailField(max_length=200, verbose_name="邮箱"),
        ),
        migrations.AlterField(
            model_name="user",
            name="password",
            field=models.CharField(max_length=200, verbose_name="密码"),
        ),
        migrations.AlterField(
            model_name="user",
            name="username",
            field=models.CharField(max_length=200, verbose_name="账号"),
        ),
    ]