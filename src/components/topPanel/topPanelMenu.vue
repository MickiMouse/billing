<template>
    <v-navigation-drawer color="secondary"
                         app
                         fixed
                         clipped
                         v-model="menuVisible">
        <v-divider/>
        <v-list dense class="pt-0">
            <v-list-tile>
                <v-list-tile-content>
                    <v-list-tile-title>
                        <span>Меню</span>
                    </v-list-tile-title>
                </v-list-tile-content>
            </v-list-tile>
            <v-list-tile
                    v-for="item in items"
                    :key="item.title"
                    :to="item.route"
            >
                <v-list-tile-action>
                    <v-icon>{{ item.icon }}</v-icon>
                </v-list-tile-action>
                <v-list-tile-content>
                    <v-list-tile-title>{{ item.title }}</v-list-tile-title>
                </v-list-tile-content>
            </v-list-tile>
        </v-list>
    </v-navigation-drawer>
</template>

<script>
    export default {
        name: "topPanelMenu",
        props:{

        },
        data(){
            return{
                items: [
                    {title: 'Модули', icon: 'assignment',route: 'modules'},
                    {title: 'Профиль', icon: 'person', route: 'profile'}
                ],
            }
        },
        watch: {

        },
        computed: {
            menuVisible: {
                get () {
                    return this.$store.getters.menuVisible;
                },
                set (val) {
                    console.log('set');
                    this.$store.commit('set',{type: 'MenuVisible', items: val});
                }
            }
        }
    }
</script>

<style scoped>

</style>