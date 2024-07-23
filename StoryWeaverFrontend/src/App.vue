<script setup>


</script>
<script>
import Profile from "@/components/Profile.vue";
import Login from "@/components/Login.vue";
import Home from "@/components/Home.vue";


export default {
  components: {
    Profile,
    Login,
    Home
  },
  data: () => ({
    localStorage: localStorage
  }),
  computed: {
    token() {
      return this.localStorage.getItem('token');
    }
  }
}
</script>

<template>
  <div>
    <div v-if="localStorage.getItem('token')">
      <Home />
    </div >
    <div v-else>
      <Login />
    </div>
  </div>


</template>

<style scoped>

</style>
