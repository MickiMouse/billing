import Vue from 'vue'
import Router from 'vue-router'


Vue.use(Router)
const router = new Router({
    mode: 'history',
    routes: [
        { path: '/', redirect: { name: 'modules' }},
        {
            path: '/modules',
            name: 'modules',
            component: () => import('./views/Home/Home.vue'),
            meta:{
                title: 'Модули',
            },
            children:[

            ]
        },
        {
            path: '/profile',
            name: 'profile',
            component: () => import('./views/Profile/Profile.vue'),
            meta:{
                title: 'Профиль',
            },
        },
        {
            path: '/modules/:id',
            name: 'lessons',
            component: () => import('./views/Modules/Modules.vue'),
            meta:{
                title: 'Уроки'
            }
        }
    ]
});
router.beforeEach((to, from, next) => {
    console.log(to);
    document.title = to.meta.title + ' | SMART-TV';
    next()
});
export default router;

