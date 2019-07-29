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
        {
            path: '/subscribers',
            name: 'subscribers',
            component: () => import('./views/Subscribers/Subscribers.vue'),
            meta:{
                title: 'Subscribers',
            },
            children:[

            ]
        },
        {
            path: '/cards',
            name: 'cards',
            component: () => import('./views/Cards/Cards.vue'),
            meta:{
                title: 'cards',
            },
            children:[

            ]
        },
        {
            path: '/packages',
            name: 'packages',
            component: () => import('./views/Packages/Packages.vue'),
            meta:{
                title: 'packages',
            },
            children:[

            ]
        },
        {
            path: '/resellers',
            name: 'resellers',
            component: () => import('./views/Resellers/Resellers.vue'),
            meta:{
                title: 'resellers',
            },
            children:[

            ]
        },
        {
            path: '/reports',
            name: 'reports',
            component: () => import('./views/Reports/Reports.vue'),
            meta:{
                title: 'reports',
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

