export default {
    state: {
       isSuperuser: false,
    },
    mutations: {

    },

    getters: {
        isSuperuser(state) {
            return state.isSuperuser;
        },
    }
};