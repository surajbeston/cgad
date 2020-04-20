<template>
<b-container fluid>
    <b-row class = "align-items-start">
        <b-col md = "0"   xl ="2"> 
            <Left />
        </b-col>
        <b-col md="12"  xl ="7">
            <Center />
        </b-col>
        <b-col md ="0" xl ="3">
            <Right />
        </b-col>
    </b-row>
</b-container>
</template>

<script>

import Center from "~/components/middle-center.vue"
import Left from "~/components/middle-left.vue"
import Right from "~/components/middle-right.vue" 
 
export default {
    components :{
        Center,
        Right
    }
}

</script>

<style scoped>




</style>

