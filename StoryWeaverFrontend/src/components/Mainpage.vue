<template>
    <div class="main-content">
      <div class="message-box">Your main content here...</div>
    </div>
  </template>
  
  <script>
  export default {
    name: "Mainpage"
  };
  </script>
  
  <style scoped>
  .main-content {
    flex: 1;
    background-color: #2a2a2a;
    padding: 20px;
    box-sizing: border-box;
  }
  .message-box {
    background-color: #4b4b4b;
    padding: 20px;
    border-radius: 10px;
    color: #fff;
  }
  </style>
  