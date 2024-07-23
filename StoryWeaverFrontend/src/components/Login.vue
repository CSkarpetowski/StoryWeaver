<script setup>
  const name = "Login";
</script>

<script>
import axios from 'axios';
import { useRouter } from 'vue-router';
import { render } from 'vue';
export default {
  name: "Login",
  setup() {
    const router = useRouter();
    return { router }
  },
  methods:{
    getLoginData() {
      this.username = document.getElementById('username').value;
      this.password = document.getElementById('password').value;
      this.login();
    },
    login() {
      axios.post('http://localhost:8000/auth/login', {
        username: this.username,
        password: this.password

      },{headers:{
        'Content-Type': 'application/x-www-form-urlencoded'
      }})
      .then((response) => {
        const token = response.data.access_token;
        localStorage.setItem('token', token);
        console.log(response.data);
        this.$router.push('/profile');
        window.location.reload();
      }, (error) => {
        console.log(error.response.data)
        console.log(error);
        console.log(this.password);
      });
    }
  },
  data: () => ({
    username: '',
    password: ''
    
  })
}
</script>

<template>

  <label for="username">
    <input type="text" id="username">
  </label>
  <label for="password">
    <input type="password" id="password">
  </label>
  <button @click="getLoginData">Login</button>


</template>

<style scoped>

</style>