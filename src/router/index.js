import { createRouter, createWebHistory } from 'vue-router'
import HomeView from "@/views/HomeView.vue";
import ClassSearchView from "@/views/ClassSearchView.vue";
import SkillSearchView from "@/views/SkillSearchView.vue";
import NotFoundView from "@/views/NotFoundView.vue";

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes: [
        {
            path: '/',
            name: 'home',
            component: HomeView
        },
        {
            path: '/classes',
            name: 'classes',
            component: ClassSearchView
        },
        {
            path: '/skills',
            name: 'skills',
            component: SkillSearchView
        }
    ]
});

export default router;
