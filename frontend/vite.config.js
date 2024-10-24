import {defineConfig} from 'vite'
import vue from '@vitejs/plugin-vue'
import {resolve} from 'path'
// https://vitejs.dev/config/

export default defineConfig({
    plugins: [
        vue(),
    ],
    build: {
        // 多页面打包配置
        rollupOptions: {
            input: {
                // 配置所有页面路径，使得所有页面都会被打包
                main: resolve(__dirname, 'index.html'),
                user: resolve(__dirname, 'user/index.html'),
                game: resolve(__dirname, 'game/index.html'),
            }
        }
    }
})
