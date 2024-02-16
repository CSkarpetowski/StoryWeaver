<script setup>


</script>
<script>
import Profile from "@/components/Profile.vue";
import Login from "@/components/Login.vue";


export default {
  components: {
    Profile,
    Login
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
      <Profile />
    </div >
    <div v-else>
      <Login />
    </div>
  </div>


</template>

<style scoped>

</style>
