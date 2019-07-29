import Vue from 'vue'
import Router from 'vue-router'


Vue.use(Router)
const router = new Router({
    mode: 'history',
    routes: [
        { path: '/', redirect: { name: 'dashboard' }},
        {
            path: '/dashboard',
            name: 'dashboard',
            component: () => import('./views/Home/Home.vue'),
            meta:{
                title: 'dashboard',
            },
            children:[

            ]
        },
    ]
});
router.beforeEach((to, from, next) => {
    console.log(to);
    document.title = to.meta.title + ' | SMART-TV';
    next()
});
export default router;

