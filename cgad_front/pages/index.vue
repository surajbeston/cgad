<template>
  <div>
    <Header />
    <Middle />
  </div>
</template>

<style scoped>
  div{
    overflow-x: hidden;
  }
</style>

<script>

import Header from "~/components/top.vue"
import Middle from "~/components/middle.vue"
export default {
  components: {
    Header,
    Middle
  }
}
</script>