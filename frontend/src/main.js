import Vue from 'vue'
import './plugins/vuetify'
import './plugins/vuetify'
import App from './App.vue'
import router from './router'
import store from './store/store'
import 'material-icons'
import VueApexCharts from 'vue-apexcharts'
import VueSession from 'vue-session'
import axios from 'axios'
Vue.use(VueSession)
Vue.config.productionTip = false
Vue.use(VueApexCharts)
Vue.component('apexchart', VueApexCharts)
<<<<<<< HEAD
Vue.prototype.$hostname = 'http://localhost:8000';
=======
Vue.prototype.$hostname = 'http://157.230.98.28';

>>>>>>> 9a88edb4061b327e92f28d3fe2cfe3d82e6926fb
new Vue({
    router,
    store,
    render: h => h(App)
}).$mount('#app');
