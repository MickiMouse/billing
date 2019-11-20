import Vue from 'vue'
import Router from 'vue-router'


Vue.use(Router)
const router = new Router({
    mode: 'history',
    routes: [
        { path: '/', redirect: { name: 'login' }},
        {
            path: '/register',
            name: 'register',
            component: () => import('./views/Register/Register.vue'),
            meta:{
                title: 'Register',
            },
        },
        {
            path: '/login/:token',
            name: 'login token',
            component: () => import('./views/Login/Login.vue'),
            meta:{
                title: 'Login',
            },
        },
        {
            path: '/login',
            name: 'login',
            component: () => import('./views/Login/Login.vue'),
            meta:{
                title: 'Login',
            },
        },
        {
            path: '/forgot',
            name: 'forgot',
            component: () => import('./views/Login/LoginForgotPassword.vue'),
            meta:{
                title: 'Login',
            },
        },
        {
            path: '/password/:token',
            name: 'forgot',
            component: () => import('./views/Login/LoginForgotPassword.vue'),
            meta:{
                title: 'Login',
            },
        },
        {
            path: '/dashboard',
            name: 'dashboard',
            component: () => import('./views/Home/Home.vue'),
            meta:{
                title: 'Dashboard',
            },
        },
        {
            path: '/subscribers',
            name: 'subscribers',
            component: () => import('./views/Subscribers/Subscribers.vue'),
            meta:{
                title: 'Subscribers',
            },
        },
        {
            path: '/subscribers/:id/details',
            name: 'subscribers details',
            component: () => import('./views/Subscribers/SubscribersDetails.vue'),
            meta: {
                title: 'Subscribers',
            },
        },
        {
            path: '/subscribers/:id/edit',
            name: 'subscribers edit',
            component: () => import('./views/Subscribers/SubscribersEdit.vue'),
            meta: {
                title: 'Subscribers',
            },
        },
        {
            path: '/cards',
            name: 'cards',
            component: () => import('./views/Cards/Cards.vue'),
            meta:{
                title: 'Cards',
            },
        },
        {
            path: '/cards/:id/details',
            name: 'cards details',
            component: () => import('./views/Cards/CardsDetails.vue'),
            meta: {
                title: 'Cards',
            },
        },
        {
            path: '/packages',
            name: 'packages',
            component: () => import('./views/Packages/Packages.vue'),
            meta:{
                title: 'Packages',
            },
        },
        {
            path: '/packages/:id/details',
            name: 'packages details',
            component: () => import('./views/Packages/PackagesDetails.vue'),
            meta: {
                title: 'Packages',
            },
        },
        {
            path: '/resellers',
            name: 'resellers',
            component: () => import('./views/Resellers/Resellers.vue'),
            meta:{
                title: 'Resellers',
            },
        },
        {
            path: '/resellersActivation',
            name: 'resellers activation',
            component: () => import('./views/Resellers/ResellersActivation.vue'),
            meta:{
                title: 'Resellers',
            },
        },
        {
            path: '/resellers/:id/details',
            name: 'resellers details',
            component: () => import('./views/Resellers/ResellersDetails.vue'),
            meta: {
                title: 'Resellers',
            },
        },
        {
            path: '/resellers/:id/edit',
            name: 'resellers edit',
            component: () => import('./views/Resellers/ResellersEdit.vue'),
            meta: {
                title: 'Resellers',
            },
        },
        {
            path: '/reports',
            name: 'reports',
            component: () => import('./views/Reports/Reports.vue'),
            meta:{
                title: 'Reports',
            },
        },
    ]
});
router.beforeEach((to, from, next) => {
    document.title = to.meta.title + ' | Ripple';
    next()
});

export default router;

