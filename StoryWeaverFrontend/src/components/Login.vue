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
      this.email = document.getElementById('email').value;
      this.password = document.getElementById('password').value;
      this.login();
    },
    login() {
      axios.post('http://localhost:8000/auth/login', {
        email: this.email,
        password: this.password
      })
      .then((response) => {
        const token = response.data.access_token;
        localStorage.setItem('token', token);
        console.log(response.data);
        this.$router.push('/profile');
        window.location.reload();
      }, (error) => {
        console.log(error);
      });
    }
  },
  data: () => ({
    email: '',
    password: ''
  })
}
</script>

<template>

  <label for="email">
    <input type="text" id="email">
  </label>
  <label for="password">
    <input type="password" id="password">
  </label>
  <button @click="getLoginData">Login</button>


</template>

<style scoped>

</style>