<template>
  <div>
    <Header />
    <Middle />
    <Footer />
  </div>
</template>

<style scoped>
  div{
    overflow-x: hidden;
  }
</style>

<script>
import Vue from 'vue';

const EventBus = new Vue();


import Header from "~/components/top.vue"
import Middle from "~/components/middle.vue"
import Footer from "~/components/bottom.vue"
export default {
  components: {
    Header,
    Middle,
    Footer
  },
  mounted(){
      
  }
}
</script>
