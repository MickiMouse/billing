export default {
    state: {

    },
    mutations: {

    },

    getters: {
      globalProgress(state,rootState){
          console.log(rootState.LessonsCount,rootState.PassedLessonsCounter)
          return Math.floor(rootState.PassedLessonsCounter / rootState.LessonsCount * 100);
      }
    }
};