<template>
    <div class="footer-buttons">
      <button class="footer-button">Button 1</button>
      <button class="footer-button">Button 2</button>
      <button class="footer-button">Button 3</button>
      <button class="footer-button">Button 4</button>
      <button class="footer-button">Button 5</button>
      <button class="footer-button">Button 6</button>
    </div>
  </template>
  
  <script>
  export default {
    name: "UserInput"
  };
  </script>
  
  <style scoped>
  .footer-buttons {
    display: flex;
    justify-content: space-around;
    background-color: #2a2a2a;
    padding: 20px;
  }
  .footer-button {
    background-color: #4b4b4b;
    border: none;
    color: #fff;
    padding: 10px 20px;
    border-radius: 5px;
    cursor: pointer;
  }
  .footer-button:hover {
    background-color: #5c5c5c;
  }
  </style>
  