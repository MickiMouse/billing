import Vue from 'vue'
import Vuetify from 'vuetify/lib'
import 'vuetify/src/stylus/app.styl'

Vue.use(Vuetify, {
    iconfont: 'md',
    theme: {
        primary: '#007bff',
        secondary: '#f9f9ff',
        accent: '#2a73ed',
        error: '#f44336',
        warning: '#ff5722',
        info: '#00bcd4',
        success: '#8bc34a'
    },
})