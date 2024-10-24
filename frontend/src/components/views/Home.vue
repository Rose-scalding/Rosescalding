<template>
    <div>
        <nav>
            <button @click="logout">登出</button>
            <h2>用户：</h2>
        </nav>
        <h2>欢迎来到主页面！！！</h2>
        <button>游戏</button>
    </div>
</template>

<script>
export default {
    name: 'Home',
    methods: {
        logout() {
            localStorage.removeItem('token');
            this.$router.push({name: 'Login'});
        },
    }
}
</script>
<style scoped>
button {
    padding: 10px 20px;
    font-size: 16px;
    cursor: pointer;
}
</style>