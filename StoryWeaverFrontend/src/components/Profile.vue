<script>
export default {
  name: "Profile",

  methods:{
    deleteToken() {
      localStorage.removeItem('token');
      window.location.reload();
    }
  },

  Props:{

  }
}


</script>

<template>
<h1>This is after auth</h1>
<button @click="deleteToken">DeleteToken</button>

</template>

<style scoped>

</style>