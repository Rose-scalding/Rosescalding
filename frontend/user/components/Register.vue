<template>
    <h2>注册页面</h2>
    <div>
        <div style="display: flex; flex-direction: column; align-items: center; justify-content: center; height: 50vh;">
            <el-input v-model="name" style="width: 240px; margin-bottom: 10px;" placeholder="用户名"/>
            <el-input v-model="username" style="width: 240px; margin-bottom: 10px;" placeholder="账号"/>
            <el-input v-model="password" style="width: 240px; margin-bottom: 10px;" placeholder="密码" type="password"/>
            <el-input v-model="email" style="width: 240px; margin-bottom: 10px;" placeholder="邮箱"/>
            <el-input v-model="captche" style="width: 240px; margin-bottom: 10px;" placeholder="验证码"/>
            <div>
                <el-button @click="get_captche" type="primary" :disabled="isButtonDisabled">{{ buttonText }}</el-button>
                <el-button @click="register" type="primary">注册</el-button>
            </div>
        </div>

    </div>
</template>

<script>
import axios from 'axios';

export default {
    name: 'Login',
    data() {
        return {
            name: '',
            username: '',
            password: '',
            email: '',
            captche: '',
            isButtonDisabled: false,  // 按钮是否被禁用
            buttonText: "获取验证码",  // 按钮的文本
            timer: null,  // 计时器
            countdown: 60  // 倒计时时间，默认60秒
        };
    }
    ,
    methods: {
        register() {
            axios.post('http://localhost:8000/api/user/register/', {
                name: this.name,
                username: this.username,
                password: this.password,
                email: this.email,
                captche: this.captche,
            }).then(response => {
                console.log('User registered:', response.data);
                this.$router.push({name: 'Login'});
            }).catch(error => {
                console.log(error);
            });
        },
        get_captche() {
            if (!this.email) {
                this.$message.error("请输入邮箱地址");
                return;
            }
            console.log("Sending email:", this.email);  // 打印 email
            axios.post('http://localhost:8000/api/user/get_captche/', {
                email: this.email
            }).then(response => {
                console.log("验证码已经发送！");
                // 禁用按钮并开始倒计时
                this.isButtonDisabled = true;
                this.buttonText = `${this.countdown}秒后重新获取`;
                // 启动倒计时
                this.timer = setInterval(() => {
                    this.countdown--;
                    if (this.countdown > 0) {
                        this.buttonText = `${this.countdown}秒后重新获取`;
                    } else {
                        // 倒计时结束，重置按钮状态
                        clearInterval(this.timer);
                        this.isButtonDisabled = false;
                        this.buttonText = "获取验证码";
                        this.countdown = 60;  // 重置倒计时时间
                    }
                }, 1000);
            }).catch(error => {
                console.log(error);
            })
        }
    },
}
;
</script>
