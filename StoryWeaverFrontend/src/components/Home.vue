<template>
    <div class="home">
      <Sidebar />
      <main class="main">
        <MainContent />
        <UserInput />
      </main>
    </div>
  </template>
  
  <script>
  import Sidebar from "@/components/Sidebar.vue";
  import MainContent from "@/components/Mainpage.vue";
  import UserInput from "@/components/UserInput.vue"
  
  export default {
    name: "Home",
    components: {
      Sidebar,
      MainContent,
      UserInput
    }
  };
  </script>
  
  <style scoped>
  .home {
    display: flex;
    height: 100vh;
    overflow: hidden;
  }
  .main {
    display: flex;
    flex-direction: column;
    flex: 1;
  }
  </style>
  