import Vue from 'vue'
import './plugins/vuetify'
import './plugins/vuetify'
import App from './App.vue'
import router from './router'
import store from './store/store'
import 'material-icons'
import VueApexCharts from 'vue-apexcharts'
import VueSession from 'vue-session'
Vue.use(VueSession)
Vue.config.productionTip = false
Vue.use(VueApexCharts)
Vue.component('apexchart', VueApexCharts)
Vue.prototype.$hostname = 'https://3d6933a2.ngrok.io';

new Vue({
    router,
    store,
    render: h => h(App)
}).$mount('#app');
