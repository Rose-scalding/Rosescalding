import {createApp} from 'vue';
import User from './App.vue';
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'
import router from './router/index.js'// 确保这里导入的是正确的路由配置

const app = createApp(User);

// 使用路由
app.use(router);

// 使用element-plus组件
app.use(ElementPlus)

// 挂载应用
app.mount('#app');
