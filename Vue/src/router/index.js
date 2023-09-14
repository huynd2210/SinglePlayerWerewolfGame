import { createRouter,createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import History from '../views/History.vue'
import Notes from '../views/Notes.vue'
import Settings from '../views/Settings.vue'

const router = createRouter({
    history: createWebHistory(),
    routes: [
        {
            path: '/',
            component: Home
        },
        {
            path: '/chat',
            component: History
        },
        {
            path: '/notes',
            component: Notes
        },
        {
            path:'/settings',
            component: Settings
        }
    ]
})

export default router