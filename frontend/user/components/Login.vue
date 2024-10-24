<template>
    <div>
        <h2>登录页面</h2>
        <div style="display: flex; flex-direction: column; align-items: center; justify-content: center; height: 50vh;">
            <el-input v-model="email" style="width: 240px" placeholder="邮箱"/>
            <el-input v-model="password" style="width: 240px" placeholder="密码" type="password"/>
            <el-button @click="login" type="primary">登录</el-button>
            <router-link :to="{name:'Register'}">
                <h2>没有账号？点击我前去注册！</h2>
            </router-link>
        </div>
    </div>
</template>

<script>
import axios from 'axios';

export default {
    name: 'Login',
    data() {
        return {
            email: '',
            password: '',
        };
    },
    methods: {
        login() {
            axios.post('http://localhost:8000/api/user/login/', {
                email: this.email,
                password: this.password,
            }).then(response => {
                const token = response.data.access;
                localStorage.setItem('token', token); // 存储 token
                axios.defaults.headers.common['Authorization'] = `Bearer ${token}`; // 设置 Authorization 头
                // 跳转到其他页面
                this.$router.push({name: 'Home'});
            }).catch(error => {
                console.log("登陆失败！", error);
            });
        },
    },
    getCookie(name) {
        const value = `; ${document.cookie}`;
        const parts = value.split(`; ${name}=`);
        if (parts.length === 2) return parts.pop().split(';').shift();
    },
};
</script>
