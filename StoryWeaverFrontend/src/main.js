import './assets/main.css'

import { createApp } from 'vue'
import App from './App.vue'

import VueJwtDecode from "vue-jwt-decode";
import * as VueRouter from 'vue-router';
import Login from './components/Login.vue';
import Profile from './components/Profile.vue';
import Home from './components/Home.vue';

const router = VueRouter.createRouter({
  history: VueRouter.createWebHashHistory(),
  routes: [
    { path: '/', component: Login },
    { path: '/profile', component: Profile, meta: { requiresAuth: true }},
    { path: '/Home', component: Home}
  ]
})

const isTokenValid = () => {
  const token = localStorage.getItem('token');
  if (!token) {
    return false;
  }
  const decodedToken = VueJwtDecode.decode(token);

  return decodedToken.exp > Date.now() / 1000;
}

router.beforeEach((to, from, next) => {
  if (to.meta.requiresAuth && !isTokenValid()) {
    const token = localStorage.getItem('token');
    if (!token) {
      next({ path: '/' });
} else {
      next();
    }
  }
})

const app = createApp(App)
app.use(router)
app.mount('#app')

