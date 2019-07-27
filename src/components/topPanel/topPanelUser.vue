<template>
    <div class="topPanelUser" justify-end>
        <v-btn fab
               dark
               medium
               color="purple"
               to="/profile"
        >
            <span class="white--text headline">{{this.$store.getters.nameFirstLetter}}</span>
            <!--<v-icon light>person</v-icon>-->
        </v-btn>
    </div>
</template>

<script>
    export default {
        name: "topPanelUser",
        data: () => ({
            dialog: false
        })
    }
</script>

<style scoped lang="scss">

</style>