import { createApp } from 'vue';
import Game from './App.vue';
import ElementPlus from 'element-plus'
import router from './router/game.js'// 确保这里导入的是正确的路由配置

const app = createApp(Game);

// 使用路由
app.use(router);

// 使用element-plus组件
app.use(ElementPlus)

// 挂载应用
app.mount('#app');
