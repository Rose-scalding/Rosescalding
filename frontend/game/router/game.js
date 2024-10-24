import {createRouter, createWebHistory} from "vue-router";
import Gobang from "../components/chess/Gobang.vue";


const routes = [
    {
        path: '/chess/gobang',
        name: 'Gobang',
        component: Gobang
    },
];


const router = createRouter({
    history: createWebHistory(),
    routes,
});

router.beforeEach((to, from, next) => {

    const loggedIn = localStorage.getItem('token');
    if (to.matched.some(record => record.meta.requiresAuth) && !loggedIn) {
        next('/login');
    } else {
        next();
    }
});

export default router;
