import Vue from 'vue'
import './plugins/vuetify'
import App from './App.vue'
import router from './router'
import store from './store/store'
import 'material-icons'
// import '../node_modules/bootstrap/dist/css/bootstrap-grid.min.css'
// import '../node_modules/bootstrap/dist/css/bootstrap.min.css'
// import '../node_modules/bootstrap/dist/css/bootstrap-reboot.min.css'

Vue.config.productionTip = false

new Vue({
    router,
    store,

    render: h => h(App)
}).$mount('#app')
