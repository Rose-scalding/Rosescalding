<template>
    <div>
        <h1>欢迎来到主页面</h1>
        <p v-if="!isLoggedIn">您还没有登录，请先登录！</p>
        <div v-else>
            <p>您已经登录，可以访问该页面。</p>
            <div>
                <a href="game/index.html">点击进入游戏页面</a>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'Home',
    data() {
        return {
            isLoggedIn: false,  // 默认未登录
        };
    },
    created() {
        const token = localStorage.getItem('token');
        if (token) {
            this.isLoggedIn = true;  // 如果有 token，表示已经登录
        }
    }
    ,
}
</script>
<style scoped>
button {
    padding: 10px 20px;
    font-size: 16px;
    cursor: pointer;
}
</style>