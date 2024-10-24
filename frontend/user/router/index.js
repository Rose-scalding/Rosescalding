import Login from '../components/Login.vue';
import Home from "../components/Home.vue";
import Register from '../components/Register.vue';
import {createRouter, createWebHistory} from 'vue-router';


const routes = [
    {
        path: '/',
        name: 'Home',
        component: Home
    },
    {
        path: '/login',
        name: 'Login',
        component: Login
    },
    {
        path: '/register',
        name: 'Register',
        component: Register
    },
];

const router = createRouter({
    history: createWebHistory(),
    routes,
});

router.beforeEach((to, from, next) => {
    const token = localStorage.getItem('token');  // 从 localStorage 获取 token

    // 检查是否需要认证
    if (to.matched.some(record => record.meta.requiresAuth)) {
        if (!token) {
            // 如果没有 token，跳转到登录页面，并提示用户
            next({
                path: '/login',
                query: {redirect: to.fullPath},  // 可选：记录用户试图访问的路径，登录后可以重定向回去
            });
            alert('您还没有登录，请先登录');
        } else {
            // 有 token，允许继续访问
            next();
        }
    } else {
        next();  // 不需要认证，继续访问
    }
});

export default router;
