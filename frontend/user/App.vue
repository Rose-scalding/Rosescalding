<template>
    <el-menu
            :default-active="activeIndex"
            class="el-menu-demo"
            mode="horizontal"
            :ellipsis="false"
            @select="handleSelect"
    >
        <el-menu-item index="0">
            <img
                    style="width: 100px"
                    src="../user/images/img.png"
                    alt="Element logo"
            />
        </el-menu-item>
        <!--        <div v-if="isLoggedIn">-->
        <router-link :to="{name:'Home'}">
            <el-menu-item index="1">
                <el-text class="mx-1" type="primary">主页</el-text>
            </el-menu-item>
        </router-link>
        <router-link :to="{name:'Login'}">
            <el-menu-item index="1">
                <el-text class="mx-1" type="primary">登录</el-text>
            </el-menu-item>
        </router-link>
        <router-link :to="{name:'Register'}">
            <el-menu-item index="2">
                <el-text class="mx-1" type="primary">注册</el-text>
            </el-menu-item>
        </router-link>
        <!--        </div>-->
        <el-menu-item index="3">
            <el-text @click="logout" class="mx-1" type="primary">登出</el-text>
        </el-menu-item>
    </el-menu>
    <div class="app">
        <div>
            <router-view/>
        </div>
    </div>
</template>

<script>
export default {
    name: 'User',
    data() {
        return {
            isLoggedIn: false
        }
    },
    methods: {
        logout() {
            localStorage.removeItem('token');
            this.$router.push({name: 'Login'});
        },
        checkLogin() {
            // 这里可以通过 API 请求或检查本地存储来验证登录状态
            const token = localStorage.getItem('authToken'); // 示例：从 localStorage 获取 token
            this.isLoggedIn = !!token; // 如果存在 token，则认为用户已登录
        }
    }

};
</script>

<style>
.el-menu--horizontal > .el-menu-item:nth-child(1) {
    margin-right: auto;
}
</style>
