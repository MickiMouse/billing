export default {
    state: {
        name: 'Михаил',
        surname: 'Гайворонский',
        passedLessonsCounter: 29,
        lastLesson: 3
    },
    mutations: {

    },

    getters: {
        Name(state) {
            return state.name;
        },
        Surname(state){
            return state.surname;
        },
        Fullname(state){
            return `${state.name} ${state.surname}`
        },
        Progress(state){
          return state.progress;
        },
        PassedLessonsCounter(state){
            return state.passedLessonsCounter;
        },
        nameFirstLetter(state){
            return state.name.slice(0,1)
        }
    }
};