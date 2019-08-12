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
// import '../node_modules/bootstrap/dist/css/bootstrap-grid.min.css'
// import '../node_modules/bootstrap/dist/css/bootstrap.min.css'
// import '../node_modules/bootstrap/dist/css/bootstrap-reboot.min.css'

Vue.config.productionTip = false
Vue.use(VueApexCharts)
Vue.component('apexchart', VueApexCharts)
Vue.prototype.$hostname = '';
new Vue({
    router,
    store,

    render: h => h(App)
}).$mount('#app')
