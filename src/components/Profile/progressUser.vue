<template>
    <v-progress-circular
            :rotate="-90"
            :size="70"
            :width="9"
            :value="value"
            :color="color"
    >
        {{ value }}
    </v-progress-circular>
</template>

<script>
    export default {
        name: "progressUser",
        props: {
            value: Number,
        },
        computed: {
            color: function(){
                let color;
                switch (true) {
                    case this.value>=0 && this.value <=49:
                        color = 'red';
                        break;
                    case this.value>=50 && this.value <=89:
                        color = 'orange';
                        break;
                    case this.value>=89:
                        color = 'green';
                        break;
                    default:
                        color = 'red';
                }
                return color;
            }
        }
    }
</script>

<style scoped>

</style>