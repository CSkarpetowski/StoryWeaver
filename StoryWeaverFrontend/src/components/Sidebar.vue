<template>
    <div class="sidebar">
      <div class="user-info">
        <img src="@/assets/user-icon.png" alt="User Icon" class="user-icon" />
        <span class="username">Username</span>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: "Sidebar"
  };
  </script>
  
  <style scoped>
  .sidebar {
    width: 250px;
    background-color: #4b4b4b;
    padding: 20px;
    height: 100vh;
    box-sizing: border-box;
  }
  .user-info {
    display: flex;
    align-items: center;
  }
  .user-icon {
    width: 40px;
    height: 40px;
    border-radius: 50%;
    margin-right: 10px;
  }
  .username {
    color: #fff;
    font-weight: bold;
  }
  </style>
  