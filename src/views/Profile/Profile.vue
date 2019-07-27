<template>
    <v-content>
        <v-container fluid px-0 py-0>
            <v-layout>
                <v-flex d-flex xs12 py-0>
                    <v-parallax
                            height="300"
                            src="https://cdn.vuetifyjs.com/images/parallax/material2.jpg"
                    >
                        <v-layout
                                align-center
                                column
                                justify-center
                        >
                            <v-btn fab
                                   dark
                                   large
                                   color="purple"
                            >
                                <span class="white--text headline">{{this.$store.getters.nameFirstLetter}}</span>
                                <!--<v-icon light>person</v-icon>-->
                            </v-btn>
                            <h3 class="font-weight-light">{{this.$store.getters.Fullname}}</h3>
                            <h5 class="font-weight-medium">{{this.progressStatusName}}</h5>
                        </v-layout>
                    </v-parallax>
                </v-flex>
            </v-layout>
        </v-container>
        <v-container fluid grid-list-md pt-0>

            <v-layout row wrap  pt-4 pb-4>

                <v-flex d-flex sm12 md4>
                    <v-card class="v-card-profile">
                        <v-flex sm12 d-flex align-center justify-center>
                            <progress-user :value="57"></progress-user>
                        </v-flex>
                        <v-card-text class="text-xs-center">

                            <h6 class="category text-gray font-weight-thin mb-3">CEO / CO-FOUNDER</h6>
                            <h4 class="card-title font-weight-light">Alec Thompson</h4>
                            <p class="card-description font-weight-light">Don't be scared of the truth because we
                              </p>
                        </v-card-text>
                    </v-card>
                </v-flex>
                <v-flex d-flex sm12 md4>
                    <v-card class="v-card-profile">
                        <v-flex sm12 d-flex align-center justify-center>
                            <progress-user :value="42"></progress-user>
                        </v-flex>
                        <v-card-text class="text-xs-center">
                            <h6 class="category text-gray font-weight-thin mb-3">CEO / CO-FOUNDER</h6>
                            <h4 class="card-title font-weight-light">Alec Thompson</h4>
                            <p class="card-description font-weight-light">Don't be scared of the truth because we
                               </p>
                        </v-card-text>
                    </v-card>
                </v-flex>
                <v-flex d-flex sm12 md4>
                    <v-card class="v-card-profile">
                        <v-flex sm12 d-flex align-center justify-center>
                            <progress-user :value='$store.getters.globalProgress'></progress-user>
                        </v-flex>
                        <v-card-text class="text-xs-center">
                            <h6 class="category text-gray font-weight-thin mb-3"> Пройдено уроков: {{$store.getters.PassedLessonsCounter}} из {{$store.getters.LessonsCount}}</h6>
                            <p class="card-description font-weight-light">
                                Научиться можно только тому, что любишь.
                                <br>
                                <span class="category text-gray font-weight-thin mb-3">Иоганн Вольфганг Гёте</span>
                            </p>

                        </v-card-text>
                    </v-card>
                </v-flex>

            </v-layout>
            <v-layout row wrap>
                <v-flex d-flex xs12>
                    <calendar></calendar>
                </v-flex>
            </v-layout>
        </v-container>
    </v-content>

</template>


<script>
    import ProgressUser from "@/components/Profile/progressUser";
    import Calendar from "@/components/Profile/calendar";
    export default {
        name: "Profile",
        components: {Calendar, ProgressUser},
        computed: {
            progressStatusName: function(){
                let StatusName;
                switch (true) {
                    case this.$store.getters.globalProgress>=0 && this.$store.getters.globalProgress <=49:
                        StatusName = 'Новичок';
                        break;
                    case this.$store.getters.globalProgress>=50 && this.$store.getters.globalProgress <=89:
                        StatusName = 'Опытный';
                        break;
                    case this.$store.getters.globalProgress>=89:
                        StatusName = 'SMM-Гуру';
                        break;
                    default:
                        StatusName = 'Новичок';
                }
                return StatusName;
            }
        }
    }
</script>

<style scoped lang="scss">
    .v-card-profile{
        overflow: hidden;
    }
</style>