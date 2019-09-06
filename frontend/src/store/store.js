import Vue from 'vue'
import Vuex from 'vuex'
import User from './user'
import Modules from './modules'
import Progress from './progress'

Vue.use(Vuex)

export default new Vuex.Store({
    modules:[
        User,
        Modules,
        Progress
    ],
    state: {
        MenuVisible: false,
        isPREPAYMENT: false,
        currency: '$'
    },
    getters: {
        menuVisible(state){
            return state.MenuVisible;
        },
        isPREPAYMENT(state){
            return state.isPREPAYMENT;
        },
        currency(state){
            return state.currency;
        }
    },
    mutations: {
        set(state, {type, items}) {
            state[type] = items;
        }
    },
    actions: {
        switchMenu({commit}){
            let inverseValue = !this.getters.menuVisible;
            commit('set',{type: 'MenuVisible', items: inverseValue});
        }
    }
})
